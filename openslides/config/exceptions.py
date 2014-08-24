from openslides.utils.exceptions import OpenSlidesError


class ConfigError(OpenSlidesError):
    pass


class ConfigNotFound(ConfigError):
    pass
