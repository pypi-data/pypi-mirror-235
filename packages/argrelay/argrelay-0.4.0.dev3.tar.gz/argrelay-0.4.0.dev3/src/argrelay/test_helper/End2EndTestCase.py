import os
import subprocess

from icecream import ic

from argrelay.client_spec.ShellContext import (
    COMP_LINE_env_var,
    COMP_POINT_env_var,
    COMP_TYPE_env_var,
    COMP_KEY_env_var,
    UNKNOWN_COMP_KEY,
)
from argrelay.enum_desc.CompType import CompType
from argrelay.test_helper import parse_line_and_cpos
from argrelay.test_helper.ClientServerTestCase import ClientServerTestCase


def run_client_with_env_vars(
    command_name,
    env_vars,
):
    client_proc = subprocess.run(
        args = [
            command_name,
        ],
        env = env_vars,
        capture_output = True
    )
    ret_code = client_proc.returncode
    if ret_code != 0:
        raise RuntimeError
    return client_proc


class End2EndTestCase(ClientServerTestCase):
    """
    Supports FS_66_17_43_42 test_infra / special test mode #5.

    In addition to starting server via its generated file in `@/bin/` dir (what `ClientServerTestCase` does),
    this tests also runs client via the generated file.

    Effectively, this runs both client and server outside the OS process responsible for running this test
    making all assertions via exit codes, stdout, stderr - what OS can provide as output of the OS process.

    It is probably "the fattest" test possible with end-to-end coverage while still using Python.
    """

    bound_command_env_var_name = "ARGRELAY_CLIENT_COMMAND"
    default_bound_command = os.environ.get(bound_command_env_var_name, "some_command")

    def env_vars(
        self,
        test_line: str,
        comp_type: CompType,
    ):
        (command_line, cursor_cpos) = parse_line_and_cpos(test_line)
        env_vars = os.environ.copy()
        env_vars[COMP_LINE_env_var] = command_line
        env_vars[COMP_POINT_env_var] = str(cursor_cpos)
        env_vars[COMP_TYPE_env_var] = str(comp_type.value)
        env_vars[COMP_KEY_env_var] = UNKNOWN_COMP_KEY
        return env_vars

    def run_DescribeLineArgs(
        self,
        command_name,
        test_line,
    ):
        env_vars = self.env_vars(
            test_line,
            CompType.DescribeArgs,
        )
        client_proc = run_client_with_env_vars(
            command_name,
            env_vars,
        )
        stderr_str = client_proc.stderr.decode("utf-8")
        return ic(stderr_str)

    def run_ProposeArgValues(
        self,
        command_name,
        test_line,
        comp_type: CompType = CompType.PrefixShown,
    ):
        assert comp_type in [
            CompType.PrefixShown,
            CompType.PrefixHidden,
            CompType.SubsequentHelp,
            CompType.MenuCompletion,
        ]
        env_vars = self.env_vars(
            test_line,
            comp_type,
        )
        client_proc = run_client_with_env_vars(
            command_name,
            env_vars,
        )
        stdout_str = client_proc.stdout.decode("utf-8")
        return stdout_str
