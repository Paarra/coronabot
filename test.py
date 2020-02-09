healthy = []
infected = []
healthy_money = 0
infected_money = 0
for member in message.guild.members:
    if check_user(member.id, 'state') == healthy:
        healthy.append(member.name)
        healthy_money += int(check_user(member.id, 'bucks'))
    else:
        infected.append(member.name)
        infected_money += int(check_user(member.id, 'bucks'))
    description = '**Healthy**'
    for person in healthy:
        description = description + '\n' + person
    description = description + '\n **Infected**'
    for person in infected:
        description = description + '\n' + person