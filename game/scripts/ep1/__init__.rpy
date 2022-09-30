init 1 python hide in ep1:
    modules = [
        "scripts/ep1/variables",
        "scripts/ep1/labels",
    ]

    for module in modules:
        renpy.load_module(module)