# Copyright (c) 2023 Baidu, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
FineTune API
"""

from typing import Any, Dict, Optional

from qianfan.utils import _get_console_ak_sk
from qianfan.resources.api_requestor import ConsoleAPIRequestor
from qianfan.resources.typing import QfResponse

# requestor for console api
_requestor = ConsoleAPIRequestor()


class FineTune(object):
    """
    class for FineTune API
    """

    @classmethod
    def get_job(cls, task_id: int, job_id: int, **kwargs: Any) -> QfResponse:
        """
        get job details with given task_id and job_id
        """
        ak, sk = _get_console_ak_sk(**kwargs)
        response = _requestor.get_finetune_job(task_id, job_id, ak=ak, sk=sk, **kwargs)
        return response

    @classmethod
    def create_task(
        cls, name: str, description: Optional[str] = None, **kwargs: Any
    ) -> QfResponse:
        """
        create a task for sft
        """
        ak, sk = _get_console_ak_sk(**kwargs)
        response = _requestor.create_finetune_task(
            name=name, description=description, ak=ak, sk=sk, **kwargs
        )
        return response

    @classmethod
    def create_job(cls, job: Dict[str, Any], **kwargs: Any) -> QfResponse:
        """
        create a finetune job
        """
        ak, sk = _get_console_ak_sk(**kwargs)
        response = _requestor.create_finetune_job(ak, sk, **job)
        return response
