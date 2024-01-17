class datapoints:
	""" Keeps all supported data types\n
		Examples in the 2nd line are not always exhaustive
	"""		
	undefined = "Undefined"
	" Any data that does not fit into any other datapoint "
	class _internal:
		" DO NOT USE "
		is_root_node = "Root Node"
		" INTERNAL USE ONLY! No Plugin should use this. "
	class name:
		title = "Title"
		" 'Dr.', 'Mr.', 'Ms.' "
		first_name = "First Name"
		" 'Mark' 'Susan' "
		middle_name = "Middle Name"
		" 'Andrew' 'Anne' "
		last_name = "Last Name"
		" 'Smith' 'Langley' "
		full_name = "Full Name"
		" 'Dr. Mark Andrew Smith', 'Ms. Susan Anne Langley' "
	class age:
		class text:
			age = "Age (Text)"
			""" 'Twenty-six', 'Sixty-five'\n
			as in Twenty-six/Sixty-five years old"""
		class numeric:
			age = "Age (Numeric)"
			""" '26', '65'\n
			as in 26/65 years old"""
	class date_of_birth:
		generic = "Date Of Birth"
		""" '1st of March 2025', '12.05.2005', '15th March' \n
		If possible use the more specific datapoints"""
		class text:
			day = "Day Of Birth (Text)"
			" 'First', '1st', 'Second', '2nd', 'Twenty-third', '23rd' "
			month = "Month Of Birth (Text)"
			" 'March', 'April' "
		class numeric:
			day = "Day Of Birth (Numeric)"
			" '1' '2' '23' "
			month = "Month Of Birth (Numeric)"
			" '03', '04' "
			year = "Year Of Birth (Numeric)"
			" '2005', '2008' "
	class person:
		pronoun = "Pronoun"
		" 'He', 'She', 'They' "
		nationality = "Nationality"
		" 'American', 'Canadian', 'Russian' "
		ethnicity = "Ethnicity"
		" 'Black', 'White', 'Asian', 'Hispanic' "
		gender = "Gender"
		" 'Male', 'Female', 'Other' "
		class body:
			class height:
				cm = "Height (cm)"
				" '178', '154' "
				feet = "Height (ft)"
				" '5', '4' "
				inches = "Height (Inch)"
				" '60', '75' "
			class weight:
				kg = "Weight (kg)"
				" '95', '78' "
				pounds = "Weight (lbs)"
				" '140', '150' "
			biological_gender = "Gender (Biological)"
			" 'Male', 'Female', 'Intersex' "
			eye_color = "Eye Color"
			" 'Blue', 'Brown', 'Green' "
			skin_color = "Skin Color"
			""" 'Lightest' 'Very Light' 'Light' 'Fair' 'Medium' 'Tanned' 'Brown' 'Dark Brown' 'Black'\n
				(These are suggested by GPT3.5 dont blame me lol)
			"""
			hair_color = "Hair Color"
			" 'Blonde', 'Black', 'Red', 'Green' "
	class vehicle:
		type = "Vehicle Type"
		" 'Car', 'Bike', 'Plane', 'Boat' "
		color = "Vehicle Color"
		" 'black', 'red', 'blue', 'green' "
		brand = "Vehicle Brand"
		" 'BMW', 'Kia', etc "
		build_year = "Vehicle Build Year"
		" '1989', '2010' "
		class identifier:
			license_plate = "License Plate"
			"""For Cars, bikes etc\n
			'SAM 911E', 'HM 07194' """
			tail_number = "Tail Number"
			"""For Planes\n
			'7T-WHM	', 'N16-100	' """
			hull_identification_number = "Hull Identification Number (HIN)"
			"""For Boats\n
			'ABC12345D404'"""
	class location:
		latitude = "Latitude"
		" '37.275036', '37°16'30.1\"N' "
		longitude = "Longitude"
		" '-115.799632', '115°47'58.7\"W' "
		zip_code = "Zip Code"
		" '90210', '90211' "
		state_or_region = "State/Region"
		" 'Kansas', 'Pest', 'Bayern', "
		city = "City"
		" 'Manhattan', 'Monor', 'München' "
		street = "Street"
		" 'Claflin Rd', 'Kossuth Lajos u.', 'Adelheidstraße' "
		house_number = "House Number"
		" '1800 ', '74', '14' "
		apartment_number = "House Number"
		" '1', '2', '3' "
		class country:
			name = "Country Name"
			" 'Germany', 'Hungary', 'United States of America' "
			code = "Country Code"
			" 'DE', 'HU', 'USA' "
	class email:
		generic = "Generic Email"
		" '*@*.*' "
		gmail = "Gmail"
		" '*@gmail.com' "
		hotmail = "Hotmail"
		" '*@hotmail.com', '*@hotmail.co.uk', '*@hotmail.fr' "
		outlook = "Outlook Mail"
		" '*@outlook.com' "
		proton = "Proton Mail"
		" '*@proton.me', '*@protonmail.com', '*pm.me' '*@protonmail.ch' "
		yahoo = "Yahoo Mail"
		" '*@yahoo.com', '*@yahoo.fr', '*@myyahoo.com' "
		aol = "AOL Email"
		" '*@aol.com' "
		msn = "MSN Email"
		" '*@msn.com' "
		icloud = "iCloud Email"
		" '@icloud.com', '@me.com', '@mac.com' "
		# TODO | Expand list using https://email-verify.my-addr.com/list-of-most-popular-email-domains.php
	class ip:
		address_v4 = "Ip Address (v4)"
		" '192.168.123.132' "
		address_v6 = "Ip Address (v6)"
		" '0000:0000:0000:0000:0000:ffff:c0a8:7b84' "
		port = "Port"
		" '8080', 25565 "
	class hash:
		generic = "Generic Hash"
		" Any hash that does not have a dedicated datapoint "
		md5 = "Md5 Hash"
		" '8ce21631012f107953cb2f1bcf3dad29' "
		sha1 = "Sha-1 Hash"
		" 'cfb9a5cb56f4b910863ed7a4a671ced2c17f5807' "
		sha256 = "Sha-256 Hash"
		" 'ebab140b3fb81566002d832257eef15795545dbca18f679d3cb800de1da80b15' "
		bcrypt = "Bcrypt Hash"
		" '$2y$10$S2VvQQ9aqSLdNVPqvsYAteApDyQcH6YLO0qWUqqrBD2CWpqml/Pnq' "
		argon2i = "Argon2i Hash"
		" '$argon2i$v=19$m=16,t=2,p=1$SGVpbWRhbGw$kXV2SueEXeBeBpkEex6MsA' "
	class profile:
		class discord:
			class _badges:
				# TODO | replace 0's with titles
				""" DO NOT USE AS ACTUAL DATAPOINT \n
				This class is used to standartize discord badge representation """
				active_developer = 0
				partner_server_owner = 0
				discord_staff = 0
				hypesquad_events = 0
				moderator_program_alumini = 0
				early_supporter = 0
				class bug_hunter:
					normal = 0
					gold = 0
				class nitro:
					generic = 0
					class type:
						nitro = 0
						classic = 0
						basic = 0
				class server_booster:
					generic = 0
					class months:
						one = 0
						two = 0
						three = 0
						six = 0
						nine = 0
						twelve = 0
						fifteen = 0
						eighteen = 0
						twentyfour = 0
				class hype_squad:
					bravery = 0
					brilliance = 0
					balance = 0
			id = "Discord User Id"
			" '155149108183695360' "
			username = "Discord Username"
			" 'Dyno' "
			old_tag = "Discord Tag (#)"
			" 'Dyno#3861' "
			pronouns = "Discord Pronouns"
			" 'He/Him', 'She/Her', 'They/Them' "
			pfp_url = "Discord Avatar"
			" 'https://cdn.discordapp.com/avatars/155149108183695360/19a5ee4114b47195fcecc6646f2380b1.png' "
			banner_url = "Discord Banner"
			" 'https://cdn.discordapp.com/banners/204683417445466112/a6ca48aad51922940e6bc383dbd0d852.png' "
			bio = "Discord Bio"
			""" Replace new lines with "\\n" \n
			'The Discord bot to make server management and moderation easy. Follow your favorite streamers, run giveaways, and more! \\n \\n https://dyno.gg/' """
			badges = "Discord User Badges"
			""" Refer to datapoints.socialmedia.discord._badges for a list of all supported badges \n
			'[datapoints.socialmedia.discord._badges.active_developer,datapoints.socialmedia.discord._badges.hype_squad.brilliance]' """
		class youtube:
			monetized = "Youtube Monetized (Channel)"
			" 'True', 'False' "
			alias = "Youtube Alias"
			" '@JCMS_', '@Miimii' "
			channel_id = "Youtube Channel Id"
			" 'UC3jv2yNiKPOZoWLLflNOzvg', 'UCOAmvK5o2JmH0vXi3Ql_qWg' "
			subscriber_count = "Youtube Subscriber Count"
			" '125', '31364', '2135949' "
			view_count = "Youtube View Count (Global)"
			" '438', '46228', '2649476' "
			video_count = "Youtube Video Count"
			" '268', '56', '1068' "
			community_post_count = "Youtube Communty Post Count"
			" '125', '56', '1068' "
			playlist_count = "Youtube Playlist Count"
			" '125', '56', '1068' "
			pfp_url = "Youtube Avatar"
			" 'https://yt3.googleusercontent.com/83wD4pS_vVQa8g537_4YnVZPjD9vND7YC_7zrnrNcMod8ARTSbtplGOKtDn6dnRrj3C9VHC_=s176-c-k-c0x00ffffff-no-rj' "
			banner_url = "Youtube Banner"
			" 'https://yt3.googleusercontent.com/Zu8akd4ko8jflbKe0NAfAPt-VMMRAB6sGuiR1a9sOMIM0U1_5GghAjYK4T7JcLzyYDoAcZjPCA=w1707-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj' "
			bio = "Youtube Bio"
			""" Replace new lines with "\\n" \n
			'Welcome back to my channel!' 'This is my new Channel! \\n Daily uploads!!!'"""
			like_percentage = "Youtube Channel Like Percentage"
			" '89', '45' "
			dislike_percentage = "Youtube Channel Dislike Percentage"
			" '89', '45' "
			like_count = "Youtube Channel Like Count"
			" '25', '1556486' "
			dislike_count = "Youtube Channel Dislike Count"
			" '25', '1556486' "
			class video:
				monetized = "Youtube Monetized (Video)"
				" 'True', 'False' "
				id = "Youtube Video Id"
				" 'Uj2jZy9WQ3Z4H8FfYl0YyjwQ' "
				title = "Youtube Video Title"
				" 'The first 1000 subscribers!' "
				thumbnail_url = "Youtube Video Thumbnail"
				" 'https://i.ytimg.com/vi/Uj2jZy9WQ3Z4/hqdefault.jpg' "
				view_count = "Youtube Video View Count"
				" '301', '465486' "
				like_count = "Youtube Video Like Count"
				" '25', '1556486' "
				dislike_count = "Youtube Video Dislike Count"
				" '25', '1556486' "
				comment_count = "Youtube Video Comment Count"
				" '301', '496' "
				like_percentage = "Youtube Video Like Percentage"
				" '89', '45' "
				dislike_percentage = "Youtube Video Dislike Percentage"
				" '89', '45' "
				upload_date = "Youtube Video Upload Date"
				" '2022-11-11' " # TODO | replace with date thingy
				description = "Youtube Video Description"
				" 'The first 1000 subscribers! \\n So much fun!' "
				class duration:
					seconds = "Youtube Video Duration (Seconds)"
					" '3600' "
					minutes = "Youtube Video Duration (Minutes)"
					" '60' "
					hours = "Youtube Video Duration (Hours)"
					" '1' "				
		class facebook:
			id = "Facebook Id"
			""" '100481883450288', '106482883650228' """
		# class instagram:
		# class snapchat:
		# class threads:
		# class pinterest:
		# class chessdotcom:
		# class riotgames:
		# class namemc:
		# class doxbin:
		# class twoDimensions:
		# class threednews:
		# class sevenCups:
		# class eighttracks:
		# class nineGAG:
		# class aPClips:
		# class about.me:
		# class academia.edu:
		# class admireMe.Vip:
		# class airPilotLife:
		# class airbit:
		# class airliners:
		# class alik:
		# class allMyLinks:
		# class anilist:
		# class archiveofOurOwn:
		# class artStation:
		# class askFedora:
		# class askFM:
		# class audiojungle:
		# class autofrage:
		# class avizo:
		# class bLIPfm:
		# class bOOTH:
		# class bandcamp:
		# class bazarcz:
		# class behance:
		# class biggerPockets:
		# class bikemap:
		# class bioHacking:
		# class bitBucket:
		# class bitwardenForum:
		# class blogger:
		# class bodyBuilding:
		# class bookcrossing:
		# class braveCommunity:
		# class buyMeACoffee:
		# class buzzFeed:
		# class cNET:
		# class cTAN:
		# class caddyCommunity:
		# class carTalkCommunity:
		# class carbonmade:
		# class careerhabr:
		# class championat:
		# class chaos:
		# class chatujmecz:
		# class choiceCommunity:
		# class clapper:
		# class cloudflareCommunity:
		# class codecademy:
		# class codechef:
		# class codeforces:
		# class codepen:
		# class codersRank:
		# class coinvote:
		# class colourLovers:
		# class contently:
		# class coroflot:
		# class cracked:
		# class crevado:
		# class crowdin:
		# class cryptomatorForum:
		# class dEVCommunity:
		# class dMOJ:
		# class dailyMotion:
		# class dealabs:
		# class discogs:
		# class discussElasticco:
		# class disqus:
		# class docker Hub:
		# class dribbble:
		# class duolingo:
		# class eintrachtFrankfurtForum:
		# class envatoForum:
		# class erome:
		# class etsy:
		# class euw:
		# class exposure:
		# class eyeEm:
		# class f3cool:
		# class fameswap:
		# class fandom:
		# class finanzfrage:
		# class fiverr:
		# class flickr:
		# class flightradar24:
		# class flipboard:
		# class football:
		# class forumOphilia:
		# class fosstodon:
		# class freelance.habr:
		# class freelancer:
		# class freesound:
		# class g2G:
		# class gNOMEVCS:
		# class gaiaOnline:
		# class gamespot:
		# class geeksforGeeks:
		# class geniusArtists:
		# class geniusUsers:
		# class gesundheitsfrage:
		# class getMyUni:
		# class giantBomb:
		# class giphy:
		# class gitBook:
		# class gitHub:
		# class gitLab:
		# class gitee:
		# class goodReads:
		# class gradle:
		# class grailed:
		# class gravatar:
		# class gumroad:
		# class gutefrage:
		# class hEXRPG:
		# class hackTheBox:
		# class hackaday:
		# class hackerEarth:
		# class hackerNews:
		# class hackerOne:
		# class hackerRank:
		# class harvardScholar:
		# class heavyR:
		# class houzz:
		# class hubPages:
		# class hubski:
		# class iCQ:
		# class iFTTT:
		# class icons8 Community:
		# class imageFap:
		# class imgUpcz:
		# class imgur:
		# class instructables:
		# class ionic Forum:
		# class issuu:
		# class itch.io:
		# class itemfix:
		# class jellyfinWeblate:
		# class jimdo:
		# class joplinForum:
		# class kEAKR:
		# class kaggle:
		# class keybase:
		# class kik:
		# class kongregate:
		# class lOR:
		# class launchpad:
		# class leetCode:
		# class lessWrong:
		# class letterboxd:
		# class linktree:
		# class listed:
		# class liveJournal:
		# class lobsters:
		# class lolchess:
		# class lottieFiles:
		# class lushStories:
		# class mMORPGForum:
		# class mapify:
		# class medium:
		# class memrise:
		# class minecraft:
		# class mixCloud:
		# class modelhub:
		# class monkeytype:
		# class motherless:
		# class motorradfrage:
		# class myAnimeList:
		# class myMiniFactory:
		# class myspace:
		# class nICommunityForum:
		# class needrom:
		# class nextcloud Forum:
		# class nightbot:
		# class ninjaKiwi:
		# class nintendoLife:
		# class nitroType:
		# class notABug.org:
		# class nyaa.si:
		# class oGUsers:
		# class openStreetMap:
		# class opensource:
		# class ourDJTalk:
		# class pSNProfilescom:
		# class packagist:
		# class pastebin:
		# class patreon:
		# class periscope:
		# class pinkbike:
		# class pocketStars:
		# class polarsteps:
		# class polygon:
		# class polymart:
		# class pornhub:
		# class productHunt:
		# class promoDJ:
		# class rajcenet:
		# class rateYourMusic:
		# class rclone Forum:
		# class redTube:
		# class redbubble:
		# class reddit:
		# class reisefrage:
		# class replitcom:
		# class researchGate:
		# class reverbNation:
		# class roblox:
		# class rocketTube:
		# class rubyGems:
		# class rumble:
		# class runeScape:
		# class sWAPD:
		# class sbazarcz:
		# class scratch:
		# class scribd:
		# class shitpostBot5000:
		# class shpock:
		# class sketchfab:
		# class slant:
		# class slideShare:
		# class slides:
		# class smule:
		# class soundCloud:
		# class sourceForge:
		# class speedruncom:
		# class splice:
		# class sporcle:
		# class sportlerfrage:
		# class sportsRU:
		# class spotify:
		# class starCitizen:
		# class steamGroup:
		# class strava:
		# class sublimeForum:
		# class tLDRLegal:
		# class tRAKTRAIN:
		# class telegram:
		# class tellonymme:
		# class tenor:
		# class themeForest:
		# class tikTok:
		# class tnAFlix:
		# class tradingView:
		# class trakt:
		# class trashboxRU:
		# class trawelling:
		# class trello:
		# class tryHackMe:
		# class tuna:
		# class twitch:
		# class twitter:
		# class ultimateGuitar:
		# class unsplash:
		# class vK:
		# class vSCO:
		# class velomania:
		# class venmo:
		# class vero:
		# class vimeo:
		# class virgool:
		# class virusTotal:
		# class wICGForum:
		# class warriorForum:
		# class wattpad:
		# class webNode:
		# class weblate:
		# class weebly:
		# class whonixForum:
		# class wikidot:
		# class wikipedia:
		# class windy:
		# class wix:
		# class wolframalphaForum:
		# class wordPressOrg:
		# class wordnik:
		# class xboxGamertag:
		# class xvideos:
		# class youNow:
		# class youPic:
		# class zhihu:
		# class akniga:
		# class authorSTREAM:
		# class babyRU:
		# class babyblogRU:
		# class chaossocial:
		# class couchsurfing:
		# class d3RU:
		# class devRant:
		# class drive2:
		# class eGPU:
		# class fl:
		# class forumguns:
		# class freecodecamp:
		# class geocaching:
		# class gfycat:
		# class habr:
		# class hunting:
		# class iMGSRCRU:
		# class igromania:
		# class interpals:
		# class irecommend:
		# class jbzdcompl:
		# class kwork:
		# class labpentestit:
		# class lastfm:
		# class leasehackr:
		# class livelib:
		# class mastodoncloud:
		# class mastodonsocial:
		# class mastodontechnology:
		# class mastodonxyz:
		# class metacritic:
		# class moikrug:
		# class mstdnio:
		# class nairalandcom:
		# class nnRU:
		# class note:
		# class npm:
		# class opennet:
		# class osu!:
		# class phpRU:
		# class pikabu:
		# class pr0gramm:
		# class proghu:
		# class queeraf:
		# class satsisRU:
		# class sessionize:
		# class skyrock:
		# class socialtchncsde:
		# class spletnik:
		# class svidbook:
		# class toster:
		# class uid:
		# class wikivg:
			
	class sensetive_data:
		social_security_number = "Social Security Number"
	class credit_card:
		name = "Credit Card name"
		number = "Credit Card Number"
		cvc = "Credit Card CVC"
		class expiry:
			date = "Credit Card Expiry Date (mm/yyyy)"
			month = "Credit Card Expiry Date (Month)"
			year = "Credit Card Expiry Date (Year)"

	# class personal_website:
	# 	name = "Dp.Personal_Website.Name"
	# 	domain = "Dp.Personal_Website.Domain"
	# 	ip = "Dp.Personal_Website.Ip"
	# 	subdomain = "Dp.Personal_Website.Subdomain"
	# 	dns_server = "Dp.Personal_Website.Dns_Server"
	# class credentials:
	# 	numerical_pin_number = "Dp.Credentials.Numerical_Pin_Number"
	# 	password = "Dp.Credentials.Password"
	# class contact:
	# 	fax_number = "Dp.Contact.Fax_Number"
	# 	phone_number = "Dp.Contact.Phone_Number"
	# class image:
	# 	generic = "Dp.Image.Generic"
	# 	face = "Dp.Image.Face"
	# 	id = "Dp.Image.Id"

import inspect

def getDatapointbyString(value, cls=datapoints):
	for name, attribute in cls.__dict__.items():
		if isinstance(attribute, str) and str(attribute).lower().replace(" ","") == str(value).lower().replace(" ",""):
			return attribute
		elif inspect.isclass(attribute):
			result = getDatapointbyString(value, attribute)
			if result:
				return result
	return None