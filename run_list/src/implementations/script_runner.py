import subprocess
from pathlib import Path

from PythonPractice.run_list.src.constant import FAIL
from PythonPractice.run_list.src.interfaces.script_runner_interface import ScriptRunnerInterface


class ScriptRunner(ScriptRunnerInterface):
    def run_script(self, script_name: str):
        if not Path(script_name).suffix:
            script_name += ".py"
        script_path = f"../script/{script_name}"
        if not Path(script_path).exists():
            print(f"{script_path} does not exist.")
            return FAIL, script_path
        result = subprocess.run(["python", script_path], capture_output=True)
        return result.returncode, Path(script_path).name
