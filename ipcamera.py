__author__ = 'jamespcole'

import json
import time

import requests

"""
Generic IP Camera class
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This lib is designed to simplify communication with IP Cameras from home-assistant
"""

camera_types = '''
[
	{
		"model": "",
		"manufacturer": "",
		"still_image_url": "",
		"streaming_url": "",
		"zoom_in": false,
		"zoom_out": false
	}
]
'''

def get_camera(model, base_url, username, password):
	if model == 'DCS-930L':

	else
		return IpCamera()

class IpCamera(object):

	def __init__(self, model, base_url, username, password):
		#device_data = json.loads(device_data_str)
		self.model = model
		self.BASE_URL = base_url
		self.username = username
		self.password = password

		#these area all the defaults override them in derived classes
		self._still_image_url_segment = 'image.jpg'
		self._has_streaming = False
		self._streaming_url_segment = ''
		self._can_zoom = False
		self._can_pan_left = False
		self._can_pan_right = False
		self._can_pan_up = False
		self._can_pan_down = False
		self._has_night_vision = False
		self._has_motion_tracking = False


	@property
	def still_image_url_segment(self):
	    return self._still_image_url_segment
	@still_image_url_segment.setter
	def still_image_url_segment(self, value):
	    self._still_image_url_segment = value

	@property
	def still_image_url(self):
		return self.BASE_URL + '/' + self.still_image_url_segment

	@property
	def has_streaming(self):
	    return self._has_streaming
	@has_streaming.setter
	def has_streaming(self, value):
	    self._has_streaming = value

	@property
	def streaming_url_segment(self):
	    return self._streaming_url_segment
	@streaming_url_segment.setter
	def streaming_url_segment(self, value):
	    self._streaming_url_segment = value

	@property
	def streaming_url(self):
		return self.BASE_URL + '/' + self.streaming_url_segment

	@property
	def can_zoom(self):
	    return self._can_zoom
	@can_zoom.setter
	def can_zoom(self, value):
	    self._can_zoom = value
	
	@property
	def can_pan_left(self):
	    return self._can_pan_left
	@can_pan_left.setter
	def can_pan_left(self, value):
	    self._can_pan_left = value

	@property
	def can_pan_right(self):
	    return self._can_pan_right
	@can_pan_right.setter
	def can_pan_right(self, value):
	    self._can_pan_right = value

	@property
	def can_pan_up(self):
	    return self._can_pan_up
	@can_pan_up.setter
	def can_pan_up(self, value):
	    self._can_pan_up = value

	@property
	def can_pan_down(self):
	    return self._can_pan_down
	@can_pan_down.setter
	def can_pan_down(self, value):
	    self._can_pan_down = value

	@property
	def has_night_vision(self):
	    return self._has_night_vision
	@has_night_vision.setter
	def has_night_vision(self, value):
	    self._has_night_vision = value
	
	@property
	def has_motion_tracking(self):
	    return self._has_motion_tracking
	@has_motion_tracking.setter
	def has_motion_tracking(self, value):
	    self._has_motion_tracking = value

