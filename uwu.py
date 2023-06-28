import random

player_hp = 20
enemy_hp = 15

print("¡Comienza la batalla!")
print("¡El enemigo te desafía a un duelo!")

while player_hp > 0 and enemy_hp > 0:
    player_damage = random.randint(1, 6)
    enemy_damage = random.randint(1, 4)

    print("\n--- Turno del jugador ---")
    print(f"Tu HP: {player_hp}")
    print(f"HP del enemigo: {enemy_hp}")

    print("\nElige tu acción:")
    print("1. Atacar")
    print("2. Huir")

    action = input("Selecciona tu acción (1-2): ")

    if action == "1":
        print(f"\n¡Has atacado al enemigo y le has causado {player_damage} puntos de daño!")
        enemy_hp -= player_damage
    elif action == "2":
        print("\n¡Has intentado huir!")
        escape_chance = random.randint(1, 10)
        if escape_chance > 5:
            print("¡Has escapado con éxito!")
            break
        else:
            print("¡No has logrado escapar!")
    else:
        print("Acción inválida. Pierdes el turno.")

    if enemy_hp <= 0:
        print("\n¡Has derrotado al enemigo! ¡Ganas la batalla!")
        break

    print("\n--- Turno del enemigo ---")
    print(f"Tu HP: {player_hp}")
    print(f"HP del enemigo: {enemy_hp}")

    print("\nEl enemigo te ataca...")
    print(f"El enemigo te ha causado {enemy_damage} puntos de daño.")
    player_hp -= enemy_damage

    if player_hp <= 0:
        print("\n¡Has sido derrotado! ¡Has perdido la batalla!")
        break

print("\n--- Fin de la batalla ---")
