from enum import Enum

from promptmanager.PromptManager.settings.base import BASE_DIR


class ModulePath(Enum):
    PYTHON3_SCRIPT = '00000000-0000-0000-1111-000000000001', BASE_DIR / "script/python3_script.py"

    TEXT_SEGMENTATION = '00000000-0000-0000-bbbb-000000000001', BASE_DIR / "script/text_segmentation.py"
    TEXT_TRUNCATION = '00000000-0000-0000-bbbb-000000000002', BASE_DIR / "script/text_truncation.py"

    CHROMA_WRITER = '00000000-0000-0000-cccc-000000000001', BASE_DIR / "script/chroma_writer.py"
    CHROMA_READER = '00000000-0000-0000-cccc-000000000002', BASE_DIR / "script/chroma_reader.py"
    DINGO_WRITER = '00000000-0000-0000-cccc-000000000003', BASE_DIR / "script/dingodb_writer.py"
    DINGO_READER = '00000000-0000-0000-cccc-000000000004', BASE_DIR / "script/dingodb_reader.py"

    def __int__(self, module_id, script_path):
        self.module_id = module_id
        self.script_path = script_path

    @property
    def module_id(self):
        return self.module_id

    @property
    def script_path(self):
        return self.script_path

    @staticmethod
    def get_module_path_by_id(module_id: str) -> str:
        for module in ModulePath:
            if module.module_id == module_id:
                return module.script_path

        from promptmanager.exception import exception
        raise exception.FLOW_MODULE_ID_NOT_SUPPORT


