# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Vega(Component):
    """A Vega component.


Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- opt (dict; optional):
    Vega-Embed options.

- spec (dict; optional):
    A Vega or Vega-Lite spec."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_vega_components'
    _type = 'Vega'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, spec=Component.UNDEFINED, opt=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'opt', 'spec']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'opt', 'spec']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(Vega, self).__init__(**args)
