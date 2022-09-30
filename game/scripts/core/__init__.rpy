init -1 python hide in core:
    import store

    modules = [
        "scripts/core/gui",
        "scripts/core/config",
        "scripts/core/build",
    ]

    for module in modules:
        renpy.load_module(module)

init python hide in core:
    import store

    modules = [
        "scripts/core/variables",

        "scripts/core/styles",
        "scripts/core/screens",
        "scripts/core/labels",
    ]

    for module in modules:
        renpy.load_module(module)