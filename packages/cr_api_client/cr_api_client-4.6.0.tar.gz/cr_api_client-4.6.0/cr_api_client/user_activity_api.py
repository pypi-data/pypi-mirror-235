#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2021 AMOSSYS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
import json
import os
import shutil
import time
from tempfile import TemporaryDirectory
from typing import Any
from typing import Dict
from typing import List

import requests
from loguru import logger

import cr_api_client.core_api as core_api
from cr_api_client import shutil_make_archive_lock
from cr_api_client.config import cr_api_client_config


# -------------------------------------------------------------------------- #
# Internal helpers
# -------------------------------------------------------------------------- #


def _get(route: str, **kwargs: str) -> Any:
    return requests.get(
        f"{cr_api_client_config.user_activity_api_url}{route}",
        verify=cr_api_client_config.cacert,
        cert=(cr_api_client_config.cert, cr_api_client_config.key),
        timeout=30,
        **kwargs,
    )


def _post(route: str, **kwargs: str) -> Any:
    return requests.post(
        f"{cr_api_client_config.user_activity_api_url}{route}",
        verify=cr_api_client_config.cacert,
        cert=(cr_api_client_config.cert, cr_api_client_config.key),
        timeout=30,
        **kwargs,
    )


def _put(route: str, **kwargs: str) -> Any:
    return requests.put(
        f"{cr_api_client_config.user_activity_api_url}{route}",
        verify=cr_api_client_config.cacert,
        cert=(cr_api_client_config.cert, cr_api_client_config.key),
        timeout=30,
        **kwargs,
    )


def _delete(route: str, **kwargs: str) -> Any:
    return requests.delete(
        f"{cr_api_client_config.user_activity_api_url}{route}",
        verify=cr_api_client_config.cacert,
        cert=(cr_api_client_config.cert, cr_api_client_config.key),
        timeout=30,
        **kwargs,
    )


def _handle_error(result: requests.Response, context_error_msg: str) -> None:
    if result.headers.get("content-type") == "application/json":
        error_msg = result.json()["message"]
    else:
        error_msg = result.text

    raise Exception(
        f"{context_error_msg}. "
        f"Status code: '{result.status_code}'.\n"
        f"Error message: '{error_msg}'."
    )


# -------------------------------------------------------------------------- #
# Internal helpers
# -------------------------------------------------------------------------- #


def _zip_user_activity(user_activity_path: str, temp_dir: str) -> str:
    """Private function to zip a user_activity content"""
    zip_file_name = os.path.join(temp_dir, "user_activity")

    with shutil_make_archive_lock:
        shutil.make_archive(zip_file_name, "zip", user_activity_path)

    return "{}.zip".format(zip_file_name)


def get_version() -> str:
    """Return user_activity API version."""
    result = _get("/user_activity/version")

    if result.status_code != 200:
        _handle_error(result, "Cannot retrieve User activity API version")

    return result.json()


# -------------------------------------------------------------------------- #
# User activity API
# -------------------------------------------------------------------------- #


def user_activity_play(
    id_simulation: int,
    user_activity_path: str,
    debug_mode: str = "off",
    wait: bool = True,
    speed: str = "normal",
    record_video: bool = False,
    write_logfile: bool = False,
    user_activity_file_results: str = None,
) -> None:
    """Play user activity on targeted simulation."""

    logger.info(
        "[+] Playing user activity '{}' on simulation id '{}'".format(
            user_activity_path, id_simulation
        )
    )

    user_activity_success = False

    try:
        data = {
            "idSimulation": id_simulation,
            "debug_mode": debug_mode,
            "speed": speed,
            "record_video": record_video,
            "write_logfile": write_logfile,
        }

        with TemporaryDirectory(
            prefix="cyber_range_cr_user_activity_archive"
        ) as temp_dir:
            # Zipping user activity files
            zip_file_name = _zip_user_activity(user_activity_path, temp_dir)
            user_activity_files = open(zip_file_name, "rb")
            files = {"user_activity_files": user_activity_files}
            try:
                result = _post(
                    "/user_activity/start_user_activity", data=data, files=files
                )
            finally:
                user_activity_files.close()

        if result.status_code != 200:
            _handle_error(result, "Cannot start user activity at user_activity API")

        # Wait for the operation to be completed in backend
        task_id = result.json()["task_id"]

        logger.info(f"  [+] User activity task ID: {task_id}")

        user_activity_success = __handle_wait(
            wait, user_activity_file_results, id_simulation, task_id
        )
    except Exception as e:
        raise Exception("Issue when starting user activity execution: '{}'".format(e))
    finally:

        if record_video:
            path_output_video = f"/cyber-range-catalog/simulations_resources/{id_simulation}/output/user_activity/{task_id}/"
            logger.info(
                f"[+] VNC video recordings are available on compute manager at this location: {path_output_video}"
            )

        if write_logfile:
            path_output_log = f"/cyber-range-catalog/simulations_resources/{id_simulation}/output/user_activity/{task_id}/"
            logger.info(
                f"[+] Log files are available on compute manager at this location: {path_output_log}"
            )

    return (user_activity_success, task_id)


def __handle_wait(
    wait: bool, user_activity_file_results: str, id_simulation: int, task_id: str
) -> bool:
    current_status = ""
    data = {
        "task_id": task_id,
    }
    if wait:
        while True:
            # Sleep before next iteration
            time.sleep(2)

            logger.info(
                f"  [+] Currently executing user activity for simulation ID '{id_simulation}'..."
            )

            result = _get("/user_activity/status_user_activity", data=data)

            result.raise_for_status()

            result = result.json()

            if "status" in result:
                current_status = result["status"]

                if current_status == "ERROR":
                    error_message = result["error_msg"]
                    raise Exception(
                        "Error during simulation operation: '{}'".format(error_message)
                    )
                elif current_status == "FINISHED":
                    # Operation has ended
                    break

        # Get User Activity Result
        request = _get("/user_activity/result_user_activity", data=data)
        request.raise_for_status()

        result = request.json()

        user_activity_results = result["result"]
        user_activity_success = user_activity_results["success"]

        if user_activity_success:
            logger.info(
                f"[+] User activity was correctly executed on simulation ID '{id_simulation}'"
            )
        else:
            logger.error(
                f"[-] User activity was executed with errors on simulation ID '{id_simulation}'"
            )

        if user_activity_file_results is not None:
            # create file for json results
            try:
                with open(user_activity_file_results, "w") as fd:
                    json.dump(user_activity_results, fd, indent=4)

                logger.info(
                    f"[+] User activity results are available here: {user_activity_file_results}"
                )

            except Exception as e:
                logger.error(f"[-] Error while writing user activity results: {e}")

        if not user_activity_success:
            json_results = json.dumps(
                user_activity_results, indent=4, separators=(",", ": ")
            )
            raise Exception(
                f"Some action could not be played. See user activity result for more information: {json_results}"
            )
    return current_status


def user_activity_status(id_simulation: int, id_user_activity: str) -> None:
    """Get a particular user activity status on targeted simulation."""

    try:
        data = {
            "task_id": id_user_activity,
        }
        result = _get("/user_activity/status_user_activity", data=data)

        if result.status_code != 200:
            _handle_error(
                result, "Cannot get user activity status from user activity API. "
            )

        return result.json()

    except Exception as e:
        raise Exception("Issue when getting user activity status: '{}'".format(e))


def all_activities_status(id_simulation: int) -> str:
    """Get all user activities status on targeted simulation."""

    try:
        result = _get(
            "/user_activity/all_activities_status",
            headers={"Content-Type": "application/json"},
        )

        if result.status_code != 200:
            _handle_error(
                result, "Cannot get user activity status from user activity API. "
            )

        return result.json()

    except Exception as e:
        raise Exception("Issue when getting user activity status: '{}'".format(e))


def user_activity_result(id_simulation: int, id_user_activity: str) -> str:
    """Get user activity result on targeted simulation."""

    try:
        data = {
            "task_id": id_user_activity,
        }
        result = _get(
            "/user_activity/result_user_activity",
            headers={"Content-Type": "application/json"},
            data=data,
        )

        if result.status_code != 200:
            _handle_error(
                result, "Cannot get user activity result from user activity API"
            )

        return result.json()

    except Exception as e:
        raise Exception("Issue when getting user activity result: '{}'".format(e))


def orchestrator_initialize(
    id_simulation: int = 1,
    node_names: List = [],
    debug_mode: str = "off",
    record_video: bool = False,
    write_logfile: bool = False,
    user_activity_file_results: str = "",
    timeout: int = 600,
) -> str:
    """
    This function calls orchestrator_initialize and waits for successful completion.
    """
    try:
        node_cpes = []
        for node_name in node_names:
            node = core_api.fetch_node_by_name(id_simulation, node_name)
            node_cpes.append(node["cpe"])

        data = {
            "id_simulation": id_simulation,
            "node_names": str(node_names),
            "node_cpes": str(node_cpes),
            "debug_mode": debug_mode,
            "record_video": record_video,
            "write_logfile": write_logfile,
            "user_activity_file_results": user_activity_file_results,
            "timeout": timeout,
        }

        logger.debug("data = ")
        logger.debug(str(data))

        result = _post(
            "/activity_orchestrator/orchestrator_initialize",
            data=data,
        )

        if result.status_code != 200:
            _handle_error(
                result, "Cannot get user activity result from user activity API"
            )
        task_ids = result.json()["task_ids"]
        done_ids = []
        user_activity_success = False
        logger.info("[+] Initializing user activity Orchestrator:")
        while task_ids:
            # Sleep before next iteration
            logger.info("  [+] Currently initializing user activity Orchestrator...")

            time.sleep(
                10
            )  # We only query user activities' status every 10 seconds to prevent spam
            for task_id in task_ids:

                data = {
                    "task_id": task_id,
                }

                result = _get("/user_activity/status_user_activity", data=data)

                result.raise_for_status()

                result = result.json()

                if "status" in result:
                    current_status = result["status"]

                    if current_status == "ERROR":
                        error_message = result["error_msg"]
                        raise Exception(
                            "Error during simulation operation: '{}'".format(
                                error_message
                            )
                        )
                    elif current_status == "FINISHED":
                        # Operation has ended
                        task_ids.remove(task_id)
                        done_ids.append(task_id)
                        break
        for task_id in done_ids:
            data = {
                "task_id": task_id,
            }
            request = _get("/user_activity/result_user_activity", data=data)
            request.raise_for_status()

            result = request.json()
            user_activity_results = result["result"]
            if not user_activity_results["success"]:
                user_activity_success = False
                break
            logger.info("[+] Orchestrator successfully initialized.")
        return user_activity_success
    except Exception as e:
        raise Exception("Issue when getting user activity result: '{}'".format(e))


def orchestrator_run(
    timeout: int = 600,
) -> str:
    """
    This function calls orchestrator_run and does not wait for return
    """
    try:
        logger.info("[+] Running user activity orchestrator...")
        data = {
            "timeout": timeout,
        }

        result = _post(
            "/activity_orchestrator/orchestrator_run",
            data=data,
        )

        if result.status_code != 200:
            _handle_error(result, "Cannot run orchestrator.")
        logger.info("[+] Orchestrator running.")
        return result.json()

    except Exception as e:
        raise Exception("Issue when getting user activity result: '{}'".format(e))


def orchestrator_insert_high_priority_activity(
    action_name: str,
    target_name: str,
    target_os: str,
    target_pack: str,
    action_datas: Dict,
) -> str:
    """
    This function calls orchestrator_insert_high_priority_activity and does not wait for return
    """
    try:
        logger.info("[+] Inserting high priority action...")
        data = {
            "action_name": action_name,
            "target_name": target_name,
            "target_os": target_os,
            "target_pack": target_pack,
            "action_datas": json.dumps(action_datas),
        }
        logger.debug(data)

        result = _post(
            "/activity_orchestrator/orchestrator_insert_high_priority_activity",
            data=data,
        )

        if result.status_code != 200:
            _handle_error(result, "Cannot insert high priority action in orchestrator.")
        logger.info("[+] High priority action inserted.")
        return result.json()

    except Exception as e:
        raise Exception("Issue when getting user activity result: '{}'".format(e))


def orchestrator_stop() -> str:
    """
    This function calls orchestrator_stop and does not wait for return
    """
    try:

        logger.info("[+] Stopping user activity orchestrator...")

        result = _post("/activity_orchestrator/orchestrator_stop")

        if result.status_code != 200:
            _handle_error(result, "Cannot stop orchestrator.")
        logger.info("[+] Orchestrator will stop after current actions end.")
        return result.json()

    except Exception as e:
        raise Exception("Issue when stopping orchestrator: '{}'".format(e))
