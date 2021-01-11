# based on: https://github.com/ericwoolard/CS-GO-Update-Notifier

import io
import json
import os
import sys


def save(path, data_str, mode='w'):
    path = ensureAbsPath(path)
    try:
        with io.open(path, mode, encoding='utf-8') as f:
            f.write(str(data_str))
    except IOError:
        directory = os.path.dirname(path)
        if not os.path.isdir(directory):
            try:
                os.makedirs(directory)
            except OSError as oserr:
                pass
        if os.path.isdir(directory):
            return save(path, data_str, mode)
        else:
            print(f'Could not write to {path}')
            return False
    else:
        return True


def read(path):
    path = ensureAbsPath(path)
    try:
        fileContents = ''
        with open(path) as f:
            fileContents = f.read()
        return fileContents
    except IOError:
        print(f'Could not find or open file: {path}')
        return False


def ensureAbsPath(path):
    botRootDir = os.path.dirname(os.path.abspath(sys.argv[0])) + '/'
    return path if os.path.isabs(path) else botRootDir + path


def saveJson(path, data):
    return save(
        path,
        json.dumps(
            data,
            ensure_ascii=False,
            indent=4,
            separators=(',', ': ')
        )
    )


def readJson(path):
    f = read(path)
    if f:
        try:
            return json.loads(f)
        except ValueError:
            print(f'Could not parse JSON file: {path}')
            return False
    else:
        return False


def updateJsonID(path, new_id):
    jsonFile = open(path, 'r')
    data = json.load(jsonFile)
    jsonFile.close()

    tmp = data['build_ID']
    data['build_ID'] = new_id

    jsonFile = open(path, "w+")
    jsonFile.write(json.dumps(data, indent=4))
    jsonFile.close()

def updateJsonGC(path, new_gc):
    jsonFile = open(path, 'r')
    data = json.load(jsonFile)
    jsonFile.close()

    tmp = data['game_coordinator_status']
    data['game_coordinator_status'] = new_gc

    jsonFile = open(path, "w+")
    jsonFile.write(json.dumps(data, indent=4))
    jsonFile.close()
    
def updateJsonSL(path, new_sl):
    jsonFile = open(path, 'r')
    data = json.load(jsonFile)
    jsonFile.close()

    tmp = data['sessionsLogon']
    data['sessionsLogon'] = new_sl

    jsonFile = open(path, "w+")
    jsonFile.write(json.dumps(data, indent=4))
    jsonFile.close()
    
def updateJsonPC(path, new_pc):
    jsonFile = open(path, 'r')
    data = json.load(jsonFile)
    jsonFile.close()

    tmp = data['player_count']
    data['player_count'] = new_pc

    jsonFile = open(path, "w+")
    jsonFile.write(json.dumps(data, indent=4))
    jsonFile.close()
    
def updateJsonTS(path, new_ts):
    jsonFile = open(path, 'r')
    data = json.load(jsonFile)
    jsonFile.close()

    tmp = data['time_server']
    data['time_server'] = new_ts

    jsonFile = open(path, "w+")
    jsonFile.write(json.dumps(data, indent=4))
    jsonFile.close()
    
def updateJsonS(path, new_s):
    jsonFile = open(path, 'r')
    data = json.load(jsonFile)
    jsonFile.close()

    tmp = data['scheduler']
    data['scheduler'] = new_s

    jsonFile = open(path, "w+")
    jsonFile.write(json.dumps(data, indent=4))
    jsonFile.close()
    
def updateJsonSC(path, new_sv):
    jsonFile = open(path, 'r')
    data = json.load(jsonFile)
    jsonFile.close()

    tmp = data['online_server_count']
    data['online_server_count'] = new_sv

    jsonFile = open(path, "w+")
    jsonFile.write(json.dumps(data, indent=4))
    jsonFile.close()   
    
def updateJsonAP(path, new_ap):
    jsonFile = open(path, 'r')
    data = json.load(jsonFile)
    jsonFile.close()

    tmp = data['active_player_count']
    data['active_player_count'] = new_ap

    jsonFile = open(path, "w+")
    jsonFile.write(json.dumps(data, indent=4))
    jsonFile.close()
    
def updateJsonSS(path, new_ss):
    jsonFile = open(path, 'r')
    data = json.load(jsonFile)
    jsonFile.close()

    tmp = data['search_seconds_avg']
    data['search_seconds_avg'] = new_ss

    jsonFile = open(path, "w+")
    jsonFile.write(json.dumps(data, indent=4))
    jsonFile.close()
    
def updateJsonSP(path, new_sp):
    jsonFile = open(path, 'r')
    data = json.load(jsonFile)
    jsonFile.close()

    tmp = data['searching_players']
    data['searching_players'] = new_sp

    jsonFile = open(path, "w+")
    jsonFile.write(json.dumps(data, indent=4))
    jsonFile.close()
      
def updateJsonDC(path, new_dc):
    jsonFile = open(path, 'r')
    data = json.load(jsonFile)
    jsonFile.close()

    tmp = data['dev_player_count']
    data['dev_player_count'] = new_dc

    jsonFile = open(path, "w+")
    jsonFile.write(json.dumps(data, indent=4))
    jsonFile.close()
    
def updateJsonP24(path, new_p24):
    jsonFile = open(path, 'r')
    data = json.load(jsonFile)
    jsonFile.close()

    tmp = data['peak_24_hours']
    data['peak_24_hours'] = new_p24

    jsonFile = open(path, "w+")
    jsonFile.write(json.dumps(data, indent=4))
    jsonFile.close()
    
def updateJsonPA(path, new_pa):
    jsonFile = open(path, 'r')
    data = json.load(jsonFile)
    jsonFile.close()

    tmp = data['peak_all_time']
    data['peak_all_time'] = new_pa

    jsonFile = open(path, "w+")
    jsonFile.write(json.dumps(data, indent=4))
    jsonFile.close()
    
def updateJsonUQ(path, new_uq):
    jsonFile = open(path, 'r')
    data = json.load(jsonFile)
    jsonFile.close()

    tmp = data['unique_monthly']
    data['unique_monthly'] = new_uq

    jsonFile = open(path, "w+")
    jsonFile.write(json.dumps(data, indent=4))
    jsonFile.close()
