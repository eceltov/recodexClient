class AliasContainer:
    """Class that handles the resolution of presenter and handler aliases defined in aliases.yaml.
    """

    def __init__(self, definitions):
        self.definitions = definitions
        self.__presenter_suffix = '_presenter'

        self.__init_raw_resolve_dict()
        self.__init_default_aliases()

    def __init_raw_resolve_dict(self):
        # create a map from raw (with the 'presenter'/'action' prefix/suffix) presenter names to handlers
        raw_presenter_to_handler_map: dict[str, list[str]] = {}
        for operation_id in self.definitions.keys():
            presenter_pos = operation_id.find(self.__presenter_suffix)
            if presenter_pos == -1:
                raise RuntimeError(f"The operationId '{operation_id}' does not contain the '{self.__presenter_suffix}' substring")

            presenter_name = operation_id[0 : presenter_pos] + self.__presenter_suffix
            handler_name = operation_id[presenter_pos + len(self.__presenter_suffix) + 1 :]

            if presenter_name in raw_presenter_to_handler_map:
                raw_presenter_to_handler_map[presenter_name].append(handler_name)
            else:
                raw_presenter_to_handler_map[presenter_name] = [ handler_name ]
        self.raw_presenter_to_handler_map = raw_presenter_to_handler_map

    def __init_default_aliases(self):
        # maps aliases to raw presenter name
        presenter_aliases: dict[str, str] = {}
        # a list of presenter names without the '_presenter' suffix (used in 'did you mean... error messages')
        base_presenter_aliases: list[str] = []
        for presenter_name in self.raw_presenter_to_handler_map.keys():
            # keep the raw name as a valid alias
            presenter_aliases[presenter_name] = presenter_name

            # add raw name without the '_presenter' suffix
            shortened_name = presenter_name[: -len(self.__presenter_suffix)]
            presenter_aliases[shortened_name] = presenter_name

            base_presenter_aliases.append(shortened_name)
        self.presenter_aliases = presenter_aliases
        self.base_presenter_aliases = base_presenter_aliases

        # maps raw presenter names to a dict from handler aliases to raw handler names
        handler_aliases: dict[str, dict[str, str]] = {}
        # maps raw presenter names to a list of handler aliases without the 'action_' prefix
        base_handler_aliases: dict[str, list[str]] = {}
        for presenter_name, handler_names in self.raw_presenter_to_handler_map.items():
            aliases = {}
            base_aliases = []
            for handler_name in handler_names:
                # keep the raw name as a valid alias
                aliases[handler_name] = handler_name

                # add raw name without the 'action_' prefix
                shortened_name = handler_name[len('action_') :]
                aliases[shortened_name] = handler_name

                base_aliases.append(shortened_name)
            handler_aliases[presenter_name] = aliases
            base_handler_aliases[presenter_name] = base_aliases
        self.handler_aliases = handler_aliases
        self.base_handler_aliases = base_handler_aliases

    def __get_raw_presenter_name_or_throw(self, presenter):
        if presenter not in self.presenter_aliases:
            msg = f"'{presenter}' is not a known presenter name or alias. Use one of the presenters below:"
            for presenter_alias in self.base_presenter_aliases:
                msg += f"\n{presenter_alias}"
            raise RuntimeError(msg)
        return self.presenter_aliases[presenter]

    def __get_raw_handler_name_or_throw(self, presenter, handler):
        raw_presenter_name = self.__get_raw_presenter_name_or_throw(presenter)
        aliases = self.handler_aliases[raw_presenter_name]
        if handler not in aliases:
            msg = f"'{handler}' is not a known handler name or alias. Use one of the handlers below:"
            for handler_alias in self.base_handler_aliases[raw_presenter_name]:
                msg += f"\n{handler_alias}"
            raise RuntimeError(msg)
        return aliases[handler]

    def add_presenter_alias(self, presenter, alias):
        raw_presenter_name = self.__get_raw_presenter_name_or_throw(presenter)
        
        if alias in self.presenter_aliases:
            raise RuntimeError(f"The presenter alias '{alias}' is already registered"
                + f"for the '{self.presenter_aliases[alias]}' presenter")
        
        # the value has to be the raw presenter name
        self.presenter_aliases[alias] = raw_presenter_name


    def add_handler_alias(self, presenter, handler, alias):
        raw_presenter_name = self.__get_raw_presenter_name_or_throw(presenter)
        raw_handler_name = self.__get_raw_handler_name_or_throw(presenter, handler)
        aliases = self.handler_aliases[raw_presenter_name]

        if alias in aliases:
            raise RuntimeError(f"The handler alias '{alias}' is already registered"
                + f"for the '{aliases[alias]}' handler")
        
        # the value has to be the raw handler name
        aliases[alias] = raw_handler_name

    def get_operation_id(self, presenter: str, handler: str) -> str:
        """Returns an ID identifying the endpoint.

        Args:
            presenter (str): The name of the presenter or alias.
            handler (str): The name of the handler or alias.

        Raises:
            RuntimeError: Thrown when the presenter of handler could not be resolved.

        Returns:
            str: Returns an ID identifying the endpoint.
        """

        raw_presenter_name = self.__get_raw_presenter_name_or_throw(presenter)
        raw_handler_name = self.__get_raw_handler_name_or_throw(presenter, handler)
        return f"{raw_presenter_name}_{raw_handler_name}"

    def get_presenters(self) -> list[str]:
        """Returns a list of presenters in snake case without the '_presenter' suffix.

        Returns:
            list[str]: Returns a list of presenters in snake case without the '_presenter' suffix.
        """
        return self.base_presenter_aliases

    def get_handlers(self, presenter: str) -> list[str]:
        """Returns a list of handlers in snake case without the 'action_' prefix.

        Args:
            presenter (str): The presenter containing the handlers. Can be any presenter alias.

        Returns:
            list[str]: Returns a list of handlers in snake case without the 'action_' prefix.
        """
        base_presenter = self.__get_raw_presenter_name_or_throw(presenter)
        return self.base_handler_aliases[base_presenter]
