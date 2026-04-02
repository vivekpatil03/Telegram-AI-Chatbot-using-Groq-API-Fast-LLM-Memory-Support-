user_memory = {}

MAX_HISTORY = 10

def get_history(user_id):
    return user_memory.get(user_id, [])

def update_history(user_id, role, message):
    if user_id not in user_memory:
        user_memory[user_id] = []

    user_memory[user_id].append({
        "role": role,
        "content": message
    })

    # keep last N messages
    user_memory[user_id] = user_memory[user_id][-MAX_HISTORY:]