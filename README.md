# Overwatch_Lobby_Datatracking

This is Aud's code storage repo designed to hold all of Lobby Codes that he likes, modifies or creates. At the end of the day this is to serve as a learning process for both Aud and the rest of the community. Lots of this code wouldn't be possible without reading [Seita's Code](https://twitter.com/Seita_ow) and everyone sitting in my streams helping me through dumb bugs. [Twitch plug xddd](https://twitch.com/audisbad)

<br>

Special thanks to [Josh](https://twitter.com/Tschoschi90) and [Aplox](https://twitter.com/_Aplox) for setting me on the analyst path so long ago, and [Jack](https://twitter.com/Jack_di_Quadri) for helping me through the STUPIDEST of errors LOL.




# Content
## Aud's Stats Farmer
Aud's stats farmer is a lobby built off of Seita's Scrim Lobby preset. It's designed to provide your usual lobby functions, while also allowing admins to dump the stats to the Inspector. Basically the idea is to allow for people to get easier access to stats. 

### How it works
If you navigate to `/Auds_Stats_Farmer/Auds_StatsFarmer_...` you'll see a file that contains the code to the lobby. (There may be multiple files with that name, some for PTR some for Live, some for different versions... The logic inside of these programs are relativly the same, the syntax is just differet as the PTR and Live can change in how the Workshop parses code.)

<br>
The basic premis is to log `Events` to the inspector. That's it. We track these overtime to provide basically a play by play of what happened so we can do analysis of Overwatch play over certain perameters... 

<br>

**Example**: How many `Final Blows` does `John` earn across all of our maps played where `Maps` == `Eichenwald`. We would find this data by looking at all of the `Final Blow` events logged by the inspector when `Map` == `Eichenwald`


#### What are events????
`Events` in Aud Language is an event in Overwatch that we can track... Things like `Elimination`s, `Final Blow`s, `Ultimate Casted`, etc.


### Running
Basically to run that lobby code, copy the text in that file and paste it into the workshop via the past code button. (TODO: INSERT IMAGE OF THIS PROCCESS). 

<br>

After that just enter your scrim / game and play it through... **ONCE YOU FINISH THAT MAP SET** Send the lobby back to lobby, and open up the `Workshop Inspector`, then click the `copy log to clip board` button. You can now save that log to a file, from which you can convert to CSV or whatever data type you want. (TODO: INSERT IMAGE OF THIS PROCCESS AS WELL)