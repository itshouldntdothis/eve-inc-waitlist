#Changelog
* 1.7.5:
  * Prevent long SSO token from being truncated
  * Various improvements to importing data von ESI
  * Fixed complex filters in table search
* 1.7.4:
  * Fixed a typo that could prevent fits being approved
* 1.7.3:
  * Fixes:
    * Fixed adding Corporation and Alliance to whitelist
    * Fixed some problems with adding bans
* 1.7.2:
  * Fixes:
    * Allowed Corporations and Alliances to be whitelisted
* 1.7.1:
  * Fixes:
    * Fixed broken migration files
* 1.7.0:
  * Features:
    * Added UI and Database based sorting and tagging of fits
    * Added config option to have everyone banned by default, so only whitelisted characters have access
    * Added config option to disable scruffy mode disable->scruffy_mode
    * Added config option to disable public api access without login disable->public_api
  * Improvements:
    * Some messages and pages related to Teamspeak are now hidden if TS is disabled or no configuration set
    * Implemented proper merging of base and user logger config because using pythons dictConfig really isn't very good
    * If TS is disabled Teamspeak related pages do not show up anymore, if there is no active TS teamspeak related messages should not show anymore
  * Changes:
    * Updated minimum version of various python requirements
    * Made werkzeug a fix version requirement since it broke between 0.14 and 0.15 also updated to 0.15.2
    * Waitlists on frontpage now use part of the with instead of 1/4th (which made the 5th go into another row)
    * Website titles now have the community_name config option at the end
  * Fixes:
    * Sending data with some from esi forwarded 204 response
    * Wrong title on Help page
* 1.6.5:
  * Improvements:
    * Added import of market groups
  * Changes:
    * Changed loglevel of some messages
* 1.6.4:
  * Fixes:
    * fixed error that could get the waitlist SSE connection to reconnect indefinitely
* 1.6.3:
  * Fixes:
    * Dropping some more sql connections, as soon as they are not needed anymore
    * removed some delays in esi calls
    * Removed potential permanent loop trying to tell an SSE client to refresh the page
* 1.6.2:
  * Fixes:
    * Fixed some problems with refreshing tokens
* 1.6.1:
  * Fixes:
    * Fixed missing include that prevent some fittings from getting submitted
    * Fixed account page or command core page not working because they used the same bundle name
* 1.6.0:
  * Features:
    * Added option to delete a role
    * Added commandline argument to create/update config file, without starting the waitlist
  * Fixes:
    * Account Status (deactivate/activate) button does now update its state after getting clicked
    * Fixed language code sent to ESI
    * Fixed not setting the required attribute for the resisthulls skill input
    * Fixed some problems with detecting the correct waitlist group for ships that use multiple different guns
  * Improvements:
    * Various performance related improvements
    * Various HTML cleanups
    * Changed the way events are rendered on the front page, to make the html look cleaner
    * Removed some dead code
    * Various improvements to the way translations are handled
  * Changes:
    * The entry count for each list is now displayed to all users
    * Disabled assets autorebuild by default since it is simply not working correctly
    * Role changes are now logged as database relation and as json blob, should a role be deleted the json blob remains
* 1.5.6:
  * Improvements:
    * Carriers added to dps group
    * Removed now useless fileinput for TypeIds update
  * Fixes:
    * Fixed fleet view not working
  * Changes:
    * Made default logfile location the cwd
* 1.5.5:
  * Improvements:
    * Added rules for sorting titans/supers into dps
    * Added ability to parse Fighters (which are officially not included in EFT format as documented by ccp)
* 1.5.4:
  * Fixes:
    * Corrected error in databases scheme to represent dogma attributes, which blocked imports
* 1.5.3:
  * Fixes:
    * Fixed exception during ESI error handling, by calling a none existant method
* 1.5.2:
  * Fixes:
    * Fixed feedbackmessage using the wrong localization identifier
    * Fixed some problems with parsing error messages because of unversioned changes to status codes from ccps api
    * Added some workaround for errors caused by failed internals responses between esi and sso, since ccp doesn't seem to see and really need to investigate this fast
* 1.5.1:
  * Fixes:
    * Fixed an exception because of wrong restriction on database scheme
    * Improved an error message
    * Wrong iteration over weapon mods which caused unintended categorisation of fits
* 1.5.0:
  * Features
    * Translation support, current languages are english and german
      * Module infos are going to be loaded in the selected language too
    * Adjusted parsing of ingame fits for changed made to the game
    * Updated fit display library to a version that supports the ingame fit format changes too
  * Fixes
    * Some parts of the site not being readable on dark themes
    * Roles not properly getting selected in config dialog
    * Fixed sometimes displaying input for display name of waitlists when the user didn't have permission to change it
    * Fixed missing space between multiple fleetmaners/fcs
* 1.4.2:
  * Improvements
    * Community name is no longer hidden when menu collapses, also moved menu button to right side
    * Using minfied version of the fitting stats tool script now
    * Theme are now versioned like other assets allowing for easier cache control
  * Fixes:
    * Converted the date-time picker fields on comp history search to date and time native browser fields
    * Properly apply scheme to swagger spec
    * Fixed some bootstrap includes using the wrong version
    * Fixed a typo on reform page
* 1.4.1:
  * Fixes
    * Swagger spec not containing the scheme
    * Falling back to dark_purple theme instead of default when user has a theme set that does not exist anymore (if no theme set it went for default)
* 1.4.0:
  * Improvements
    * Updated bootstrap framework from 4alph6 to 4.1.1
    * Redesigned the overview page
    * Improved speed on checking account character tokens (from multiple minutes for a few hundred chars to a few seconds), by using parallel requests
  * Features:
    * There is a config option now to enable/disable showing count for approvals
    * Added statistic for members found in fleet, a characters is only counted once per UTC day
  * Fixes:
    * Bug with removing/adding alts not generating the history entry
    * CDN getting initialized even when disabled
    * Exception that could occure if you input a non existant character name in e.g. bans
* 1.3.2
  * Fixes
    * Feedbacks open ingame mail button not working (this was broken with esipy upgrade in 1.3.0)
  * Improvement
    * Intercepting ajax calls to urls with /universe/types/ in url and setting Accept-Language header to'en-us, en;q=0.9'
    to counter the change where ccp's esi started looking at that header for the name of modules
    
* 1.3.1
  * Fixes
    * fixed for possible race contition between checking if a character exists in db and creating it
    * Fixed spelling anonymous as anonymouse in crossorigin
    * Fix not beeing able to login with a transfered character
  * Changes
    * Not logging monolith errors to the error log anymore only to debug, these are expected
    * Not logging fleet invite errors that are caused by a monolith error at all anymore
* 1.3.0
  * Fixes
    * Ban for character banned users did not work when esi was not responding
    * Fix a typo in Open Mail endpoint preventing it from working
        * this did not affect anything since the waitlist did not use the feature of this codepath
    * The Edit Account Dialog now properly selects all roles an Account has, if the account has a `New` tag
    * Fix an exception that was not properly handled which prevented unknown modules to be loaded from ESI
  * Features
    * The whole token management got reworked and the waitlist can now have more then 1 token per character
      This means that e.g. you don't need to reauth evertime you change from sending a mail to taking fleet and the other way round.
    * Added config option: `app -> user_agent` to allow setting a custom user agent to use for ESI interaction
    * Reworked login management and introduced new config option: `security -> require_auth_for_chars` (Normal Visitors to the site are not an Account)
      * If this is **enabled** Waitlist Account user
        * can only set a character after poviding authentication for it
        * can login to the waitlist with any of the authenticated alts
      * If this is **disabled** Waitlist Account user
        * can only login with the Eve Character that matches their Account usnername
        * can set any Character as the character to use for the Waitlist
    * Added option for accounts with a group that has the new permission 'change_character_links' to remove and add character links for accounts
  * Improvements
    * Before assinging some one as Fleet Comp to a fleet on take over it is now check that this character has Fleet Boss on the fleet instead of just checking if he is a member of the fleet.
    * Added an AccountNote if a Account's username is changed
    * Notes now contain a jsonPayload that can hold more information e.g. the body of a mail sent etc. for old notes this info is lost
        * the migration script converts old notes to the new format and extracts as much data as possible
    * Account list download is now as json and offeres multiple options of which data should be included
* 1.2.3
  * Fixes
    * Waitlist Group can not be cleared
* 1.2.2
  * Fixes
    * Fixed eve mail part not working
    * babili minify not working on editable grid js
* 1.2.1
  * Fixes
    * Fixed use app from esipy which doesn't exist there anymore
* 1.2.0
  * Features
    * Added icon for wardec check to xup page
      - red = active wardec
      - orange = wardec starting soon
      - ? = there was an error checking
  * Fixes
    * Fixed a bug with not applying the right default theme
    * An id being used double on main page
    * updated editabletables code to hopefully workaround some bugs
      - this should also enable sorting by names
  * Changes
    * Database access has all been converted to using ORM
    * Other db reladed changes to better support different databases (like pgsql)
* 1.1.4
  * Fixes
    * Fixed error handling for invalidated refresh tokens
* 1.1.3
  * Fixes
    * Fixed error in handling sse requests
    * Fixed error when generating ESI requests
* 1.1.2
  * Fixes
    * Fixed broken html that made the page not work correctly in some browser
* 1.1.1
  * Fixes
    * Removed some unneeded code
    * Removed fix for wrong / in ESI underscore routes
* 1.1.0
  * Changes
    * Taking over a fleet now detects the fleet you are in (using new ESI route)
* 1.0.2
  * Fixes
    * fixed migration scripts to only use lowercase table names, this should fix problems with database configured to support casesensitive table names
* 1.0.1
  * Changes
    * Improved system/constellation import speed, also should properly retry failed imports now (timeouts etc.)
  * Fixes
    * Changed crest fleet link input to esi link, since ccp changed that in the client
* 1.0.0
  * Changes
    * preperations for public release
      * removing wtm references
      * changing wtm specific features to be more generalzing and configureable
      * add readme with instructions
    * updated esi swagger spec to current _latest
  * Fixes
    * Fixed esi alliance/character/corp cache not setting ids
    * trying to create config directory when it already exists
* 0.16.1
  * Changes
    * Changed Default theme to Generic Bootstrap Theme
  * Fixes
    * Fixed expressions not working on disabled groups
* 0.16.0
  * Features
    * Advanced Notification Page
  * Fixes
    * Display Name not settable to Headquarters, by restricted users
    * Some Error Messages missing styling
    * Fixed quie's script to use esi for dogma, this was deployed as hotfix onto 0.15.0
* 0.15.0
  * Features
    * New "Dark" theme with black as primary color
    * Check In button to report in fleet activity else then FC/Backseat/Fleetcomp
    * Added ability to change display name of a Waitlist
  * Fixes
     * getting character affiliations was broken and got fixed
     * popover styles for dark purple and purple fixed (font color was not readable)
     * browser support detection code was not working
* 0.14.0
  * Improvements
    * ESI error response handling centralized to have it easier to adjust them
    * Adjusted some logmessages for failed ESI calls to contain all request information
    * Moved Bootstrap up to 4.0.0-alpha6 and adjusted webpages for it
    * Added custom CSS theme
  * Fixes
    * Some urls where created wrongly because of code changing around
    * Character info not getting cached correctly (this just caused the cache to fail silently, requesting them every time)
    * Static Data Import menu entry not using correct rights to determine if it should show
    * Showing removed roles as granted on the profile in some circumstances
    * TS pokes failing some times
* 0.13.0
  * Features
    * Added caldari BS level to html data to be used by new function of quies stats tool for the waitlist
    * Log to a file if an user is requesting fitting history over a extensively long period
    * Completely new permission manager, that allows user interface configuration (this wl is really getting to much permissions :>)
    * Added "no result found" entry when no search results are found instead of leaving the table empty and people wondering if it even worked
    * Added popover to events on the front page, showing the events description instead of using the event description as the name which made them occupy a LOT of space
  * Fix
    * Account status changes not going into log
    * Fixed safety fleet move, for new esi data
    * wait time sometimes not getting correctly applied when approving a single fit
  * Change
    * Allow only  accounts with admin permission to assign admin role (before Leadership could assign any role)
    * Removed Mass Account import function that used a custom format and was not configurable
    * Removed a restrictive attribute from roles, since this was there to not allow characters with these roles to auth via IGB header and is not needed since a while (eve has no IGB anymore)
    * Some ESI interaction improvements (caching, response to errors and what not) this includes parsing monolith errors and returning them, they are not in json and looked like python literals (which has a high chance to be true since monolith is at least partial in python) so using a python literal parser now
* 0.12.2
  * Features
    * Basic trivia system that doesn't have an proper backend interface yet
  * Changes
    * Make ESI request timeout after 10s of no response
    * Fix
      * Requesting wrong/too much scopes when taking a fleet
      * Some sorting problems with the dynamic account list
* 0.12.1
  * Changes
    * Move webp support check to server side
  * Fix
    * Encoding problem when generating default configuration, related to 2.7->3.6 port
* 0.12.0
 * Changes
    * Creating Stats on the Overview page does not block the request anymore
    * Code ported from python 2.7 to python 3.6
    * XML API replaced with ESI
    * CREST API replaced with ESI
    * Default FreeMove State of a fleet is now False
  * Features
    * Added Events that get displayed on the front page, very basic ATM
    * TS3 Functionality can be disabled using a configuration option
    * Accounts that get a T/R badge assigned, get a tag that they need a welcome mail, this tag is removed if some one sends the mail to them using the waitlist
  * Fix
    * Fixed not being able to change Default Character under some circumstances
    * Fixed a bug with T-Badges not being able to take over a fleet (this was hot patched a few hour after the the 0.11 release)
* 0.11.1
  * Changes
            Added setup file for new api-scopes
* 0.11.0
  * Changes
    * Removed unused account information (mails/pw hashes got deleted)
    * Added "New" Tag to people that are added a T or R Badge or are a new account. The tag is removed if the Send Auth Mail Button is pressed on their account (they get a generated mail send using the templates)
    * Changed the way API Info is saved, so we can save which api scopes belong to them
    * Sending Mails now use ESI and sends the mail directly ! No open eve client required!
    * Added a window to see in fleet information (ships in squads and how long some one is in fleet). This is only accessible as developer role at the moment since it is mainly an experiment to see how it could be used for a future feature
  * Fixes
    * Added a missing space in Alts list
    * Fixed a typo on the waitlist page if it is down
    * corrected some loglevels SSE related logging
    * Fixed some times putting wrong (case) character names in the database when some one entered it with wrong case
  * Features
    * Added a way to download a list of all fullcommanders as a cvs format with the right permissions
    * Added a basic profile page for accounts (you need specific rights to see them)
    * People can now only press the invite button a character once per 30s, this is to prevent excessive spam
    * Added Ability for specific roles to add messages to profile pages that have a level of who can see them
      * this is mainly meant for tracking changes to positions and such
      * these notes automatically get a message added every time you change the roles some one has, use the "Add Note" filed in the dialog to make a comment as to why the roles where changed!
      * the notes get a message for when the account is created and which roles where added back then
      * they get a message added when some one sends a welcome mail to them
* 0.10.0
  * Changes
    * Comp History now shows the fit comment (which contain Logi and Caldari BS lvls)
    * Reworked the way HTML is generated out of stats to make it easier to add new ones
    * now all modules of a fit are properly saved into a table (this wasn't needed for anything before and saved a lot of expensive joins, but opens up for more selective querying), instead of just as a dna string
    * added a script to convert the dna string in existence to these table entries, and tries to best guess correct invalid dna strings, (that could be submitted by entering a dna string into the xup field) and removes module ids that refere to a id not found in the invtypeids table. Additionally if there are amounts found that are > signed int (around 2.14b) it sets the to the max value
  * Fixes
    * Fixed permissions on creating accounts from a file, was Officer, now is Leadership (Officers couldn't access the page through)
    * rearranged some js files, so there should be some size saved
* 0.9.2
  * Changes
    * Made a configuration option for using a different image server for eve images
    * added some stats to the Settings - Overview page
    * added pagination buttons to the command core list
  * Fix
    * Changed to JS to not use deprecated and in ES5+ removed ```with(variable){}``` statements so the transformation/bable works with out default settings on it
* 0.9.1
  * Features
    * Added a list that is visible to command core members and shows all roles and known alts of a person
    * Added the ability to add Notes to an Account (with the appropriate rights)
  * Changes
    * made it work in Overwolf again (their stuff is outdated but sadly there is no up to date overlay browser, maybe I should just write one)
    * Some changes to make is Safari compatible because Safari has problems with let
    * every role now has a displayName that can be different from its "actual name" this is used to display it in the command core list
  * Fix
    * I imported some wrong functions some where and it failed horribly
    * fixed some feedback center related code (made it return the right values)
* 0.9.0
  * Features
    * Added Babel and the Babili preset for js minification
    * updating fleet status using SSE events
  * Changes
    * Saving dropdown states in localstorage instead of cookies
    * rewrote and modularized most of the the JS (should yield lot better minimization now) and got rid of some ugly parts that needed to get written like that because of old IGB
    * update to boostrap-alpha5
    * added cookie security as config setting
    * fixed some typos in flashed messages
    * replaced inclusion of whole font awesome with a subset font
    * changed some default config options to use values that are more likely to work "out of the box"
    * added some preconnect tags to establish connecting to sites that we are gonna contact
  * Fixes
    * fixed entries sometimes not getting inserted in the right position (introduced with SSE)
    * added a missing js file back to the feedback page
    * fixed an exception caused by spamming the invited button  (we had those A LOT guys, stop spamming that button)
    * fixed a problem with a wrong css selector syntax that made the whole JS file not work in safari browser
    * fixed trying to reconnect to a none existing SSE endpoint when all fleets are down
* 0.8.0
  * Changes:
    * Waitlist is now autoupdating for R-Badges and linemembers
    * Removed copying username to clipboard when clicking it, since there is crest to open it ingame now
    * Removed a lot of IGB related double/workaround code
    * Gong notifications are now on the main wl page
    * X up notifications for users with fleet comp permissions
    * Base pilots are now able to view a character popup with public info (Corp & Bio)
    * No longer support IE or Edge
    * FC/Backseat/Fleetcomp (this includes taking a fleet) is now logged to a file.
    * Residents are now officially allowed to see comp history :P, Trainee's are restricted to 30min history
  * Improvements
    * Waitlist is now kept upto date using ServerSentEvents, instead of json request, less traffic, instant updates!
    * Removed extra cookies that were used to save stuff due to the ingame browsers lack of local/session storage
    * Some performance improvements for js
* 0.7.0
  * Changes
    * Frameworks updates
    * Versioning Change / Cache Optimization
    * Font Awesome Removal
* 0.6.1
  * Changes
    * You now need to login using the normal Login on the base site /
    * you need to use your Main Character (the one you Waitlist-Account is named after) for logging in
    * after you can change the character you are FC-ing with as normal
    * The Fitting display script is now part of the waitlist instead of hosted by quie (who wrote it!)
  * Improvements
    * CSS/JS files now get combined/minimized should improve page load speed a bit, reduce traffic a lot
    * minimizing JSON output a bit more
    * minimizing HTML now
* 0.6.0
  * Features
    * Fleetsettings now contain a "Safety" button
      * Moves all members of the fleet you click on to the set Safety channel (Channel is configured over TeamSpeak settings)
      * you need to be the fleetcomp of the fleet
    * API endpoint to trigger the Safety move
* 0.5.0
  * Features
  * New Bro Tag on History
  * Allow T-Badges/R-Badges to see comp history
  * Out of Game Send mail button (new CREST API came last patch)
  * Feedback backend was changed, to make it more organized and extendable for the future
  * Implemented an interface to the new mail CREST endpoint
* 0.4.2 Hotfix 1
  * fixed searches for line member names (not accounts) erroring out  because i forgot 2 dots
* 0.4.2
  * Features
    * Font size button to Comp-History (well it was there for a while because I wanted to show it to people :P but officially added in this version)
    * Copy Charactername to clipboard if you click it on the waitlist (no idea if that actually works, I can't remember actually testing it out, and browsers have some weird restrictions to clipboard access) But my commits say I added that at some point....
    * Clicking Charactername in OOG Browser should open the characters profile ingame, if you are crest authenticated with the remote UI right (take over a fleet to get it :P), if not well ofc not right?
    * Made Names in the history search match partially instead of complete
  * Fixes
    * Fixed some log messages...
* 0.4.1
  * Fixes
    * Single fit approvals getting filtered out by the "show only approvals filter" (it actually only showed entry approvals)
* 0.4.0
  * Features
    * Eve SSO login for linemembers
    * Mass Fleetinvite Tool
      * Post list of names press start when you asigned to a fleet and they will all get an invite (it is magic)
      * Use it for ez reform?
    * Added Search for Fleetcomp history where it can be filtered by Accountname, Charactername(for the target of an action) types of actions and time frame.
      * multiple account/character names can we inputed like this ```Bruce Warhead|Beryl Slanjava``` "|" is the seperator, multiple names are allways an OR since 1 action can not be done by multiple people anyway
    * Added Admin setting to insert html into page headers
    * Comp History has a button now to hide everything except fit approvals :)
  * Changes
    * images server used for player and ship pics from image.eveonline.com to imageserver.eveonline.com since the latter is a CDN and apparently supports https now
    * Display current active TSs config in the settings form (passwords excluded)
    * Show logout button to linemembers now since it is not auto relogin (with ingame browser headers) any more
    * removed alt="Charname" from character pics since it wouldn't have the space to display it anyway
  * Fixes
    * stop lossing logfiles by rotating them on restart and deleting the old one from that day (I blame wired python documentation)
    * broken logging line that was causing an error....
    * a lot of errors that could occur
* 0.3.2
  * Features
    * Auto detection of squads/wings for the fleetsetup
  * Changes
    * Increased time waiting for making a member check after an invite by 5s
    * logging improvements
    * TS Pokes stopping to work if to many people with wrong TS names failed their pokes bc of it
  * Fixes
    * After login, redirect to page that you wanted to visit originally instead of index
    * default config file creating being broke
    * using HQ MOTD for VGs
    * reusing wrong fleet connections from cache, stopping invites/member check from working
* 0.3.1
  * Features
    * Propagate "default" waitlist constellation/dock/system changes to all waitlists. Apparently people where moving to wrong systems because people started a assault/vg fleet and those weren't up-to-date
    * Display your current characters portrait next to the logout link to help know which character is currently connected to your waitlist account
    * Added Update Button to fits, for linemembers, bc apparently it is hard to x-up a new fit first and afterwards delete the old one
  * Changes
    * Don't display TS port on website if it is the default one
    * improved the wording on how you should name yourself on TeamSpeak to have pokes working
    * Only display missed invites if they are > 0
    * Don't go through the fleet setup if some one takes over an existing fleet, and was not CREST authenticated already
    * Display current character as fleetcomp instead of waitlist account name
    * Only replace Fleet MOTD on setup if it is very short < 50 characters
    * Added Option to reassign squads
    * Made waitlist be displayed as tabs instead of a drop-down, for better exposure for all fleets
    * Display all waitlistgroups for selection when setting up a fleet, not only the open ones
    * Hide the conversation button in out-of-game browser, since it doesn't work there anyway
  * Fixes
    * Made waitlists open and closable on mobile browsers
    * X-UP form always send people to the default waitlist
    * Missed invite count not getting auto updated
    * Event for a player removing himself from X-Up was missing a conversion to a display message
    * Fixed missed invites taking up a whole line in the entry
    * Improved handling of TeamSpeak disconnect detection
    * Default mails topic was always set to its body instead
    * Fixed the last squad on the priority list always getting ignored
    * Missed invited counter getting increased 2 times
    * If a name is not found on TeamSpeak, search for it with a * in front to support deaf members
    * CREST request failed bc of () out of place
    * Multiple exceptions fixed on spam clicking buttons (and trying to remove/move things that where already)
    * Fixed some exceptions related to fleetsetup and made them display useful messages. These only happened if you did weird things, like not fill out fields, use the back button on your browser or did not select a waitlistgroup since you didn't open any first
    * remember fleet id from first entry when some one goes through CREST authentication in-between
* 0.3.0
  * Features
    * Implemented CREST based invites
    * TeamSpeak Pokes
    * Customizable Mails for waitlist link (t-badge, r-badge, other)
    * Made HG/Assault and VG MOTD configure able via settings webpage
  * Changes
    * moved disabled accounts to end of list
    * reordered fields in account page to make most useful things come first
    * Changed CDN used for jquery away from google since it seems to make problems with Chinese people having a block
    * Made Fleetinvites and Notifications distinguishable in comp history, this was needed because of crest invites
    * Changed Notifications to be able to be triggered multiple times
    * Changed the look of buttons, to make it more clear what they do
  * Fixes:
    * Fixed waitlists not getting displayed correctly if default one is not open
