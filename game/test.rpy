label test:
    "[gc_pc.archetype]: LVL: [gc_pc.stats.lvl] - HP: [gc_pc.stats.current_hp] / [gc_pc.stats.base_hp] - ATK: [gc_pc.stats.base_attack] - DEF: [gc_pc.stats.base_defense] - INT: [gc_pc.stats.base_intelligence] - RES: [gc_pc.stats.base_resistance] - WIS: [gc_pc.stats.base_wisdom] - SPD: [gc_pc.stats.base_speed] - AGR: [gc_pc.stats.aggression]"
    menu:
        "Level":
            $ gc_pc.stats.level_up()
            jump test
        "Exit":
            return