#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Telegram Python API

@author: Alexis M.
@version: 0.2
"""

import requests

class telegram():
    
    def __init__(self, token, chatid = None):
        self.token = token
        self.setChatid(chatid)
        self.URL = f"https://api.telegram.org/bot{token}/"
    
    def setChatid(self, chatid):
        """
        Set the current chatid to use for following messages.

        Parameters
        ----------
        chatid : int
            Chat id.

        Returns
        -------
        None.

        """
        
        self.chatid = chatid
        
    def _hasChatid_(self):
        """
        Checks if a chatid is set or not.

        Returns
        -------
        bool
            Result of the test.

        """
        
        if self.chatid is None:
            return False
        return True
    
    def sendMessage(self, message, chatid = None):
        """
        Send a message to the given chatid.

        Parameters
        ----------
        message : str
            Message to send.
        chatid : int
            Chat id.

        Returns
        -------
        None.

        """
        
        if not self._hasChatid_() and chatid is None:
            raise ValueError("Chatid is not set or given")
            
        elif chatid is None:
            chatid = self.chatid
        
        command_URL = self.URL+"sendMessage"
        
        payload = {
            "chat_id": chatid,
            "text": message,
            }
        
        res = requests.post(command_URL, json = payload)
        res = res.json()
        
        if not res['ok']:
            raise RuntimeError(f"Unable to send message\n\tError code: {res['error_code']}\n\tDescription: {res['description']}")
            
    def sendPhoto(self, filepath, chatid = None):
        """
        Send a photo to the given chatid

        Parameters
        ----------
        filepath : path
            Path to the photo.
        chatid : int
            Chat id.

        Returns
        -------
        None.

        """
        
        if not self._hasChatid_() and chatid is None:
            raise ValueError("Chatid is not set or given")
            
        elif chatid is None:
            chatid = self.chatid
        
        command_URL = self.URL+"sendPhoto"
        
        payload = {
            "chat_id": chatid,
            }
        
        with open(filepath, 'rb') as photo:
            files = {'photo': photo}
        
            res = requests.post(command_URL, payload, files = files)
            
        res = res.json()
        
        if not res['ok']:
            raise RuntimeError(f"Unable to send message\n\tError code: {res['error_code']}\n\tDescription: {res['description']}")
    
    def getUpdates(self):
        """
        Retrieve updates.

        Returns
        -------
        None.

        """
        
        command_URL = self.URL+"getUpdates"
        
        payload = {
            "allowed_updates": ["message"]
            }
        
        update = requests.post(command_URL, json = payload)
        self.last_update = update.json()
        
