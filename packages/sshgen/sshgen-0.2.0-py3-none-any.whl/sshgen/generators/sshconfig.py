#!/usr/bin/env python
import copy
from pathlib import Path

from sshgen.logger import init_logger
from sshgen.models.host import HostModel
from sshgen.utils.file import FileUtils

log = init_logger(__name__)


class SSHConfig:
    def __init__(self, models: list[HostModel], output_file: Path | None = None):
        self.raw_models = models
        self.template_path = FileUtils.as_package_file('templates/ssh_config.template')
        self.ssh_template = self._open_template()
        self.output_file = output_file

    def generate(self) -> None:
        filtered_models: list[HostModel] = self._filter_models()
        configs: list[str] = [self._process(m) for m in filtered_models]
        self._save_config(configs)

    def _filter_models(self) -> list[HostModel]:
        temp_models = copy.deepcopy(self.raw_models)
        return [model for model in temp_models if not (model.meta_fields and model.meta_fields.skip)]

    def _process(self, model: HostModel) -> str:
        temp = self.ssh_template.replace('{{ host }}', model.host) \
            .replace('{{ hostname }}', model.ansible_host) \
            .replace('{{ host_comment }}', model.host_group) \
            .replace('{{ ssh_user }}', model.ansible_user)

        if model.meta_fields:
            if model.meta_fields.aliases:
                temp = temp.replace('{{ host_alias }}', ' '.join(model.meta_fields.aliases))
            if model.meta_fields.auth_type and model.meta_fields.auth_path:
                temp = temp.replace('{{ identification }}',
                                    f'{model.meta_fields.auth_type} {model.meta_fields.auth_path}')

        fallback_auth = '\n'.join(self._get_fallback_auth())
        temp = temp.replace('{{ identification }}', fallback_auth).replace('{{ host_alias }}', '')

        return temp

    def _open_template(self) -> str:
        return self.template_path.read_text()

    def _save_config(self, templates: list[str]) -> None:
        self._create_output_file()
        self.output_file.write_text('\n'.join(templates))
        log.info('Generated SSH config file was saved to %s', self.output_file)

    def _create_output_file(self) -> None:
        self.output_file.touch(exist_ok=True)

    @staticmethod
    def _get_fallback_auth() -> list[str]:
        parameter = 'IdentitiesOnly yes'
        width = len(parameter) + 4
        return ['IdentityFile ~/.ssh/ssh_key', f'{parameter: >{width}}']
