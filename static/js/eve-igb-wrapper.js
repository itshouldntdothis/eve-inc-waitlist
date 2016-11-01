'use strict';

if (!waitlist) {
	var waitlist = {};
}

/**
 * wrapper for eve igb fuctions
 */
waitlist.IGBW = (function() {

	var urls = {
		openwindow: waitlist.base.getMetaData('api-igui-openwindow-ownerdetails'),
		newmail: waitlist.base.getMetaData('api-igui-openwindow-newmail')
	};

	/**
	 * Opens information window for the given item, oog it opens chruker.dk if only typeID is given
	 * @param typeID id for the type of the item id can be corporationID, allianceID, factionID, characterID, a celestial ID like regionID or solarSystemID 
	 */
	function showInfo(typeID, itemID) {
		if (typeof itemID === "undefined") {
			window.open("http://games.chruker.dk/eve_online/item.php?type_id="+typeID, "_blank");
		} else {
			$.post({
				'url': urls.openwindow,
				'data': {
					'characterID': itemID,
					'_csrf_token': waitlist.base.getMetaData('csrf-token')
				},
				'error': function(data) {
					var message = data.statusText;
					if (typeof data.message !== 'undefined') {
							message += ": " + data.message;
					}
					waitlist.base.displayMessage(message, "danger");
				}
			});
		}
	}

	/**
	 * Opens a mailwindow either igbapi or crest
	 * with the given topic, mail as body and charId as recipiant
	 * @param charId Character Id of the recipiant
	 * @param subject Mails Subject
	 * @param body Mails Body
	 */
	function sendMail(charId, subject, body) {
		$.post({
			'url': urls.newmail,
			'data': {
				'_csrf_token': waitlist.base.getMetaData('csrf-token'),
				'mailRecipients': charId,
				'mailBody': body,
				'mailSubject': subject
			},
			'error': function(data) {
				var message = data.statusText;
				if (typeof data.message !== 'undefined') {
						message += ": " + data.message;
				}
				waitlist.base.displayMessage(message, "danger");
			}
		});
	}

	return {
		sendMail: sendMail,
		showInfo: showInfo
	};
}());