# Write your code here
player_class = "Wizard"
player_attack = 35
player_defense = 13
enemy_attack = 28
enemy_defense = 16

player_attack_power = player_attack * player_defense
enemy_attack_power = enemy_attack * enemy_defense

damage_dealt = player_attack_power - enemy_attack_power

combat_log = f"{player_class.upper()} has suffered {damage_dealt} damage."

is_player_stronger = player_attack_power > enemy_attack_power
is_balanced = player_defense == enemy_defense

class_initial = player_class[0]
class_code = player_class[0:3].lower()
