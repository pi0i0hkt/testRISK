
# Copyright 2020 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import logging
import random
from flask import Flask, request

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
logger = logging.getLogger(__name__)

app = Flask(__name__)
moves = ['F', 'T', 'L', 'R']

@app.route("/", methods=['GET'])
def index():
    return "Let the battle begin!"

@app.route("/", methods=['POST'])
def move():
    request.get_data()
    logger.info(request.json)
    return moves[random.randrange(len(moves))]

if __name__ == "__main__":
  app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
  
#package main
def var (
	// 左右後
	NPosition = []string{W, E, S}
	SPosition = []string{E, W, N}
	EPosition = []string{N, S, W}
	WPosition = []string{S, N, E}
	)
	
def RandStringRunes(int, letterRunes string) string {
	b := make([]byte, n)
	for i := range b {
		b[i] = letterRunes[rand.Intn(len(letterRunes))]
	}
	return string(b)
}

/*
{
  "_links": {
    "self": {
      "href": "https://https://testrisk-xiy34zjfwa-uc.a.run.app"
    }
  },
  "arena": {
    "dims": [4,3], // width, height
    "state": {
      "https://A_PLAYERS_URL": {
        "x": 0, // zero-based x position, where 0 = left
        "y": 0, // zero-based y position, where 0 = top
        "direction": "N", // N = North, W = West, S = South, E = East
        "wasHit": false,
        "score": 0
      }
      ... // also you and the other players
    }
  }
}
*/

type PersonState struct {
	URL       string
	X         int
	Y         int
	Direction string
	WasHit    bool
	Score     int
}

def var (
	board [][]*PersonState
	me    *PersonState
)

def checkHasPerson(x, y int) bool {
	if x < 0 || x >= len(board[0]) || y < 0 || y >= len(board) {
		return false
	}
	return board[y][x] != nil
}

def checkHasPersonInLeft(x, y int, direction string) bool {
	switch direction {
	case N:
		return checkHasPersonInNextPosition(x, y, NPosition[0])
	case S:
		return checkHasPersonInNextPosition(x, y, SPosition[0])
	case E:
		return checkHasPersonInNextPosition(x, y, EPosition[0])
	case W:
		return checkHasPersonInNextPosition(x, y, WPosition[0])
	}
	return false
}

def checkHasPersonInRight(x, y int, direction string) bool {
	switch direction {
	case N:
		return checkHasPersonInNextPosition(x, y, NPosition[1])
	case S:
		return checkHasPersonInNextPosition(x, y, SPosition[1])
	case E:
		return checkHasPersonInNextPosition(x, y, EPosition[1])
	case W:
		return checkHasPersonInNextPosition(x, y, WPosition[1])
	}
	return false
}

def checkHasPersonInBack(x, y int, direction string) bool {
	switch direction {
	case N:
		return checkHasPersonInNextPosition(x, y, NPosition[2])
	case S:
		return checkHasPersonInNextPosition(x, y, SPosition[2])
	case E:
		return checkHasPersonInNextPosition(x, y, EPosition[2])
	case W:
		return checkHasPersonInNextPosition(x, y, WPosition[2])
	}
	return false
}

def checkHasPersonInNextPosition(x, y int, direction string) bool {
	switch direction {
	case N:
		return checkHasPerson(x, y-1)
	case S:
		return checkHasPerson(x, y+1)
	case E:
		return checkHasPerson(x+1, y)
	case W:
		return checkHasPerson(x-1, y)
	}
	return false
}

def checkHasPersonInDirection(x, y int, direction string) bool {
	switch direction {
	case N:
		for i := 1; i < 4; i++ {
			if checkHasPerson(x, y-i) {
				fmt.Println("checkHasPersonInDirection", x, y-i)
				return true
			}
		}
		return false
	case S:
		for i := 1; i < 4; i++ {
			if checkHasPerson(x, y+i) {
				fmt.Println("checkHasPersonInDirection", x, y+i)
				return true
			}
		}
		return false
	case E:
		for i := 1; i < 4; i++ {
			if checkHasPerson(x+i, y) {
				fmt.Println("checkHasPersonInDirection", x+i, y)
				return true
			}
		}
		return false
	case W:
		for i := 1; i < 4; i++ {
			if checkHasPerson(x-i, y) {
				fmt.Println("checkHasPersonInDirection", x-i, y)
				return true
			}
		}
		return false
	}
	return false
}

def isBuilding(x, y int, direction string) bool {
	switch direction {
	case N:
		return y == 0
	case S:
		return y == len(board)-1
	case E:
		return x == len(board[0])-1
	case W:
		return x == 0
	}
	return false
}

def getPOST(w http.ResponseWriter, req *http.Request) {
	w.WriteHeader(http.StatusOK)

	j := make(map[string]interface{})
	_ = json.NewDecoder(req.Body).Decode(&j)

	dims := j["arena"].(map[string]interface{})["dims"].([]interface{})

	width := int(dims[0].(float64))
	height := int(dims[1].(float64))

	board = make([][]*PersonState, height)
	for i := 0; i < height; i++ {
		board[i] = make([]*PersonState, width)
	}

	for k, v := range j["arena"].(map[string]interface{})["state"].(map[string]interface{}) {
		x := int(v.(map[string]interface{})["x"].(float64))
		y := int(v.(map[string]interface{})["y"].(float64))
		score := int(v.(map[string]interface{})["score"].(float64))
		personState := &PersonState{
			URL:       k,
			X:         x,
			Y:         y,
			Direction: strings.ToUpper(v.(map[string]interface{})["direction"].(string)),
			WasHit:    v.(map[string]interface{})["wasHit"].(bool),
			Score:     score,
		}

		board[personState.Y][personState.X] = personState
		if personState.URL == j["_links"].(map[string]interface{})["self"].(map[string]interface{})["href"].(string) {
			me = personState
		}
	}

	fmt.Println(board)

	fmt.Println(me)

	var m string

	if checkHasPersonInDirection(me.X, me.Y, me.Direction) {
		fmt.Println("Has person In Direction")
		m = T
	} else {
		fmt.Println("No person In Direction")
		m = RandStringRunes(1, "FFRL")
	}

	if isBuilding(me.X, me.Y, me.Direction) {
		m = RandStringRunes(1, "RL")
	}

	fmt.Println(m)

	w.Write([]byte(m))

}
