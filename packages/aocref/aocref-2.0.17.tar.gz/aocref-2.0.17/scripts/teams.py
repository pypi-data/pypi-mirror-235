"""Query Liquipedia API for data updates."""
import logging
import json
import time
import re
import aiohttp
import asyncio
from collections import defaultdict

import pycountry
import requests
from ruamel.yaml import YAML
import wikitextparser as wtp
from liquipedia import db

BLACKLIST = ['simtom']
LOGGER = logging.getLogger(__name__)


def strip_leading_double_space(stream):
    if stream.startswith("  "):
        stream = stream[2:]
    return stream.replace("\n  ", "\n")


MANUAL = {
    'CZ': {'Skull'},
    'Hot Young Masters': {'Dr.Kozmonot', 'Ubetnir'},
    'One Punch': {'fatman'},
    'Dark Empire': {'Xhing'},
    'İstanbul Wildcats': {'Kasva'},
    #'Clown Legion': {'Blackheart'}
}

async def main():
    logging.basicConfig(level=logging.INFO)

    yaml = YAML()
    yaml.indent(sequence=4, offset=2)
    yaml.preserve_quotes = True
    with open('data/players.yaml', 'r') as handle:
        player_data = yaml.load(handle)
    with open('data/teams.json', 'r') as handle:
        team_data = json.loads(handle.read())
    by_id = {}
    for t in team_data:
        by_id[t['id']] = t['name'].replace(" (team)", "")

    names = set()
    result_data = defaultdict(set)
    for p in player_data:
        names.add(p['name'].lower().replace('_', '').replace(' ', ''))
        if 'liquipedia' in p:
            names.add(p['liquipedia'].lower().replace('_', '').replace(' ', ''))
    LOGGER.info("starting data update")
    for x, y in MANUAL.items():
        result_data[x] |= y
    async with aiohttp.ClientSession() as session:
        for x, y in (await db.squadplayers(session)).items():
            result_data[x.replace("_", " ").split(" (")[0]] |= y
        for x, y in (await db.teams(session)).items():
            result_data[x.replace("_", " ").split(" (")[0]] |= y

    #for x, y in fetch(SQUAD_CONDITIONS, SQUAD_PROPS).items():
    #    result_data[x] |= y
    #time.sleep(WAIT_SECS)
    #for x, y in fetch(PLAYER_CONDITIONS, PLAYER_PROPS).items():
    #    result_data[x] |= y
    #for p in player_data:
    #    if 'team' in p and 'liquipedia' not in p:
    #        result_data[by_id[p['team']]].add(p['name'])
    td = []
    id = 1
    p2t = {}
    BLACKLIST = ['MMC eSports', 'The Jedi Masters']
    PLAYER_BLACKLIST = ['DaRk_', 'Blade']
    for pp in player_data:
        if 'team' in pp:
            del pp['team']
    for x, y in result_data.items():
        if x in BLACKLIST:
            continue
        tm = {f for f in y if f.lower().replace('_', '').replace(' ', '') in names and f not in PLAYER_BLACKLIST}
        if tm:
            players = set()
            pns = set()
            for p in tm:
                ptrans = p.lower().replace('_', '').replace(' ', '')
                for pp in player_data:
                    if ptrans == pp['name'].lower().replace('_', '').replace(' ', '') or 'liquipedia' in pp and ptrans == pp['liquipedia'].lower().replace('_', '').replace(' ', ''):
                        pp['team'] = id
                        players.add(pp['id'])
                        pns.add(p)
            td.append(dict(
                name=x,
                players=sorted(list(players)),
                id=id
            ))
            id += 1
            print(x)
            print('->', pns)
    with open('data/players.yaml', 'w') as handle:
        LOGGER.info("writing new players.yaml")
        yaml.dump(player_data, handle, transform=strip_leading_double_space)
    with open('data/teams.json', 'w') as handle:
        LOGGER.info("writing new teams.json")
        handle.write(json.dumps(td, indent=2))
    LOGGER.info("finished data update")

if __name__ == '__main__':
    asyncio.run(main())
