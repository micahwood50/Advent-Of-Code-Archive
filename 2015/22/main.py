from collections import namedtuple
from heapq import heappop, heappush


FILENAME = "input.txt"


class Spell(namedtuple("BaseSpell", "name cost effect turns damage heal armor mana")):
    def __new__(
        cls,
        name: str,
        cost: int,
        *,
        effect: bool = False,
        turns: int = 0,
        damage: int = 0,
        heal: int = 0,
        armor: int = 0,
        mana: int = 0,
    ):
        return super().__new__(
            cls, name, cost, effect, turns, damage, heal, armor, mana
        )


SPELLS = [
    Spell("Magic Missile", 53, damage=4),
    Spell("Drain", 73, damage=2, heal=2),
    Spell("Shield", 113, effect=True, turns=6, armor=7),
    Spell("Poison", 173, effect=True, turns=6, damage=3),
    Spell("Recharge", 229, effect=True, turns=5, mana=101),
]


class State(object):
    def __init__(
        self,
        hp: int,
        mana: int,
        boss_hp: int,
        boss_damage: int,
        mana_spent: int = 0,
        effects: tuple[tuple[int, Spell], ...] = None,
        hard: bool = False,
        parent=None,
        spell_cast: str = None,
    ):
        self.hp = hp
        self.mana = mana
        self.boss_hp = boss_hp
        self.boss_damage = boss_damage
        self.mana_spent = mana_spent
        self.effects = effects or ()
        self.hard = hard
        self._parent = parent
        self._spell_cast = spell_cast

    def __eq__(self, other):
        if not isinstance(other, State):
            return NotImplemented

        return all(
            getattr(self, k) == getattr(other, k)
            for k in vars(self)
            if not k.startswith("_")
        )

    def __hash__(self):
        return hash(tuple(v for k, v in vars(self).items() if not k.startswith("_")))

    def iter_path(self):
        if self._parent is None:
            return

        yield from self._parent.iter_path()
        yield self._spell_cast

    def process_effects(self, hp, mana, boss_hp):
        remaining_effects = list()
        armor = 0  # either Shield is in effect or it is not

        for timer, effect in self.effects:
            hp += effect.heal
            mana += effect.mana
            boss_hp -= effect.damage
            armor = max(armor, effect.armor)

            if timer > 1:
                remaining_effects.append((timer - 1, effect))

        return tuple(remaining_effects), hp, mana, boss_hp, armor

    def boss_turn(self):
        self.effects, self.hp, self.mana, self.boss_hp, armor = self.process_effects(
            self.hp, self.mana, self.boss_hp
        )

        # only if the boss is still alive can they attack!
        if self.boss_hp > 0:
            self.hp -= max(1, self.boss_damage - armor)

    def transitions(self):
        # Player turn first
        effects, hp, mana, boss_hp, __ = self.process_effects(
            self.hp - int(self.hard), self.mana, self.boss_hp
        )

        for spell in SPELLS:
            if spell.cost > mana or any(spell is s for __, s in effects):
                # can't cast spells for which we have no mana or in effect
                continue

            new_state = State(
                hp,
                mana - spell.cost,
                boss_hp,
                self.boss_damage,
                self.mana_spent + spell.cost,
                effects,
                hard=self.hard,
                parent=self,
                spell_cast=spell.name,
            )

            if not spell.effect:
                new_state.hp += spell.heal
                new_state.boss_hp -= spell.damage

            else:
                new_state.effects = new_state.effects + ((spell.turns, spell),)

            # Boss turn next
            new_state.boss_turn()

            if new_state.hp > 0:
                yield new_state


def search_a_star(start: State) -> State | None:
    open_states = {start}
    priority_queue = [(0, start)]
    closed_states = set()
    unique_count = 0

    while open_states:
        current = heappop(priority_queue)[-1]

        if current.boss_hp < 1:
            return current

        open_states.remove(current)
        closed_states.add(current)

        for state in current.transitions():
            if state in closed_states or state in open_states:
                continue

            open_states.add(state)
            heappush(priority_queue, (state.mana_spent, unique_count, state))
            unique_count += 1


def get_input() -> tuple[int, int]:
    info_list = list()

    with open(FILENAME) as file:
        for __ in range(2):
            info_list.append(int(file.readline().split()[-1]))

    return tuple(info_list)


def part_1():
    player_hp, player_mana = 50, 500
    boss_hp, boss_damage = get_input()

    start = State(player_hp, player_mana, boss_hp, boss_damage)

    result = search_a_star(start).mana_spent

    print(f"Answer is {result}")


def part_2():
    player_hp, player_mana = 50, 500
    boss_hp, boss_damage = get_input()

    start = State(player_hp, player_mana, boss_hp, boss_damage)

    start.hard = True

    result = search_a_star(start).mana_spent

    print(f"Answer is {result}")


if __name__ == "__main__":
    part_1()
    part_2()
    pass
