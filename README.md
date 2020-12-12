# Overwatch_Lobby_Datatracking
This is  [Aud](https://twitter.com/MrCoachAud)'s code storage repo designed to hold all of Lobby Codes that he likes, modifies or creates. At the end of the day this is to serve as a learning process for both Aud and the rest of the community. Lots of this code wouldn't be possible without reading [Seita's Code](https://twitter.com/Seita_ow) and everyone sitting in my streams helping me through dumb bugs. [Twitch plug xddd](https://twitch.com/audisbad)


## Lobby Codes if you're in a hurry
- [LIVE] Converted Seita Lobby: **KVKR7**
- [LIVE] Official Games Version: **T1PHB**
- [PTR] Converted Seita Lobby: **Z6XEJ**
- [PTR] Official Games Version: **A7Y9N**
- [OPR] Converted Seita Lobby: **NEED**
- [OPR] Official Games Version: **NEED**
<br>

You can find more info on our [website](https://pro-v2.lab.insights.gg), which also happens to be the place where you can convert the logs created by this workshop to usable CSV.

# Explaining the Farmer
The farmer uses the `Log To Inspector` feature to push `Events` to a log, which the website then translates to CSV, which you can use inside of your typical spreadsheet jocky experiments if you like that stuff ;) 

You can read the detailed version of what all of that jazz means on the [site](https://pro-v2.lab.insights.gg), for this is meant to explain the code itself.


## File Structure
Each `.ow` file in the main directory represents a different variation of the Overwatch_Workshop code, some are for PTR, and LIVE builds of Overwatch and some are intended only for scrim or tournament use. 

### LIVE vs PTR
The overwatch client has 3 different versions, LIVE (or Retail), PTR (public test realm), and OPR (idk tbh, it's just the client they use for tournaments). Each client is usually on a different patch, and a different patch can mean different syntaxes, which means that code that works on the PTR client may not work on LIVE. So instead we split code up based on what client they're intended to write on, for example right now (12.11.2020) the LIVE client doesn't have the capability to write logs to a file, but the PTR client does. That means post beta released we're going to start updating PTR with features that won't work on LIVE. This file split allows us to continue providing a stable LIVE and PTR version to users.

### Scrim vs Tournament
There are two different versions of the logic flow within the Overwatch Workshop Farmer, the Scrim version and Tournament version. In short the Scrim version has all of Seita's quality of life improvements (the TEYSH lobby code) with my stats collection system written underneath allowing you to continue scrimming with ease. 

<br>
The tournament version doesn't have that at all, and is just the pure stats- It's intended for exactly what the name implies, tournaments. Or at least that's the plan :)

# Event Definitions
I'm a bit too busy to really flesh this out to where it needs to be so here's a google sheet that does sort of a good job, and the gaps can be filled in by us at the server [Sheet](https://docs.google.com/spreadsheets/d/1wkhDj_AX6Kkyy7WTaon6nTkx0dmwAGISNb6HoEtyIzI/edit?usp=sharing)

# Contributing to the project
Checkout [here](https://github.com/AudIsCool/Overwatch_Farmer/blob/main/.github/CONTRIBUTING.md) for details on how to contribute to the project!!