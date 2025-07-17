def avaliar_risco(event: str, user_agent: str) -> str:
    if "failed login" in event.lower():
        return "ALTO"
    elif "admin" in user_agent.lower():
        return "MÉDIO"
    else:
        return "BAIXO"
