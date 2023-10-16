from poetry.console.commands.install import InstallCommand


class InstallAllCommand(InstallCommand):
    name = "install-all"
    @property
    def activated_groups(self) -> set[str]:
        return {
            group.name
            for group in self.poetry.package._dependency_groups.values()
        }