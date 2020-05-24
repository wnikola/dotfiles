## Loading yml file
config.load_autoconfig()

# keybindings,
c.bindings.commands["normal"] = {"xb": "config-cycle statusbar.hide",
                                 "xt": "config-cycle tabs.show always switching"}
