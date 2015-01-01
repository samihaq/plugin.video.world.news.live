import time
import simplejson
from channel import BaseChannel, ChannelException,ChannelMetaClass, STATUS_BAD, STATUS_GOOD, STATUS_UGLY
from utils import *

############
## MTA International ##
############
        
class AlAan(BaseChannel):
    playable = True
    short_name = 'MTA'
    long_name = 'MTA International'
    default_action = 'play_stream'

    def action_play_stream(self):
        self.plugin.set_stream_url('http://mtaintl.mpl.miisolutions.net:1935/mtaintl-live-1/_definst_/mp4:Original300k.stream/playlist.m3u8')

##################
## AlJazeera EN ##
##################

class AlJazeeraEnglish(BaseChannel):
    playable = False
    short_name = 'aljazeera_en'
    long_name = 'Al Jazeera English'
    default_action = 'list_streams'
    
    def action_list_streams(self):
        data = {}
        data.update(self.args)
	data.update({'action': 'play_stream', 'Title': 'High Quality', 'stream_url': 'rtmp://aljazeeraflashlivefs.fplive.net/aljazeeraflashlive-live/ playpath=aljazeera_eng_high swfUrl="http://static.ls-cdn.com/player/5.10/livestation-player.swf" swfVfy=true live=true'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Medium Quality', 'stream_url': 'rtmp://aljazeeraflashlivefs.fplive.net/aljazeeraflashlive-live/ playpath=aljazeera_eng_med swfUrl="http://static.ls-cdn.com/player/5.10/livestation-player.swf" swfVfy=true live=true'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Low Quality', 'stream_url': 'rtmp://aljazeeraflashlivefs.fplive.net/aljazeeraflashlive-live/ playpath=aljazeera_eng_low swfUrl="http://static.ls-cdn.com/player/5.10/livestation-player.swf" swfVfy=true live=true'})
        self.plugin.add_list_item(data, is_folder=False)
        #data.update({'action': 'play_stream', 'Title': 'Mobile Quality', 'stream_url': 'http://hd2.lsops.net/live/aljazeer_en_hls.smil/playlist.m3u8'})
        #self.plugin.add_list_item(data, is_folder=False)
        self.plugin.end_list()

    def action_play_stream(self):        
        self.plugin.set_stream_url(self.args['stream_url'])

##################
## AlJazeera US ##
##################

#class AlJazeeraAmerica(BaseChannel):
#    playable = False
#    short_name = 'aljazeera_us'
#    long_name = 'Al Jazeera America'
#    default_action = 'list_streams'
    
#    def action_list_streams(self):
#        data = {}
#        data.update(self.args)
#	data.update({'action': 'play_stream', 'Title': 'High Quality', 'stream_url': 'rtmp://ajam.lsops.net/live/ playpath=ajam_en_584 swfUrl="http://static.ls-cdn.com/player/5.10/livestation-player.swf" swfVfy=true live=true'})
#        self.plugin.add_list_item(data, is_folder=False)
#        data.update({'action': 'play_stream', 'Title': 'Medium Quality', 'stream_url': 'rtmp://ajam.lsops.net/live/ playpath=ajam_en_364 swfUrl="http://static.ls-cdn.com/player/5.10/livestation-player.swf" swfVfy=true live=true'})
#        self.plugin.add_list_item(data, is_folder=False)
#        data.update({'action': 'play_stream', 'Title': 'Low Quality', 'stream_url': 'rtmp://ajam.lsops.net/live/ playpath=ajam_en_162 swfUrl="http://static.ls-cdn.com/player/5.10/livestation-player.swf" swfVfy=true live=true'})
#        self.plugin.add_list_item(data, is_folder=False)
#        data.update({'action': 'play_stream', 'Title': 'Mobile Quality', 'stream_url': 'http://ajam.lsops.net/live/ajam_en_hls.smil/playlist.m3u8'})
#        self.plugin.add_list_item(data, is_folder=False)
#        self.plugin.end_list()

#    def action_play_stream(self):        
#        self.plugin.set_stream_url(self.args['stream_url'])
        


##############
## ABC News ##
##############
        
class ABCNEWS(BaseChannel):
    playable = True
    short_name = 'abcnews'
    long_name = 'ABC News'
    default_action = 'play_stream'

    def action_play_stream(self):
        self.plugin.set_stream_url('http://abclive.abcnews.com/i/abc_live4@136330/master.m3u8?b=500,300,700,900,1200')

###############
## ABCNews24 ##
###############  

class ABCNews24(BaseChannel):
    playable = False
    short_name = 'abc24'
    long_name = 'ABC News 24'
    default_action = 'list_streams'
    
    def action_list_streams(self):
        data = {}
        data.update(self.args)
	data.update({'action': 'play_stream', 'Title': 'ABC News 24 - (Australia Only)', 'stream_url': 'http://www.abc.net.au/res/streaming/video/hls/news24.m3u8'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'ABC News 24', 'stream_url': 'rtmp://cp103653.live.edgefcs.net:1935/live?_fcs_vhost=cp103653.live.edgefcs.net&akmfv=1.8 playpath=international_medium@36382 swfVfy=true live=true'})
        self.plugin.add_list_item(data, is_folder=False)
        self.plugin.end_list()

    def action_play_stream(self):        
        self.plugin.set_stream_url(self.args['stream_url'])

##############
## BBC News ##
##############
        
#class BBCNEWS(BaseChannel):
#    playable = True
#    short_name = 'bbcnews_en'
#    long_name = 'BBC News'
#    default_action = 'play_stream'

#    def action_play_stream(self):
#        self.plugin.set_stream_url('rtmp://hd4.lsops.net/live/ playpath=bbcnews_en_364 swfUrl="http://static.ls-cdn.com/player/5.10/livestation-player.swf" swfVfy=true live=true')

####################
## BBC World News ##
####################

class BBCWORLD(BaseChannel):
    playable = True
    short_name = 'bbcworld_en'
    long_name = 'BBC World News'
    default_action = 'play_stream'

    def action_play_stream(self):
        self.plugin.set_stream_url('http://wpc.C1A9.edgecastcdn.net/hls-live/20C1A9/bbc_world/ls_satlink/b_,264,528,828,.m3u8')
        
##########
## CNBC ##
##########

class CNBC(BaseChannel):
    playable = True
    short_name = 'cnbc'
    long_name = 'CNBC'
    default_action = 'play_stream' 

    def action_play_stream(self):
        self.plugin.set_stream_url('http://livestation_hls-lh.akamaihd.net/i/cnbc_en@106428/master.m3u8')

########
## RT ##
########
        
class RT(BaseChannel):
    playable = False
    short_name = 'rt'
    long_name = 'RT'
    default_action = 'list_streams'
    
    def action_list_streams(self):
        data = {}
        data.update(self.args)
        data.update({'action': 'play_stream', 'Title': 'Global', 'stream_url': 'http://odna.octoshape.net/f3f5m2v4/cds/smil:ch1_auto.smil/playlist.m3u8'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Spanish', 'stream_url': 'http://odna.octoshape.net/f3f5m2v4/cds/smil:ch2_auto.smil/playlist.m3u8'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Arabic', 'stream_url': 'http://odna.octoshape.net/f3f5m2v4/cds/smil:ch3_auto.smil/playlist.m3u8'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'America', 'stream_url': 'http://odna.octoshape.net/f3f5m2v4/cds/smil:ch4_auto.smil/playlist.m3u8'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Documentaries', 'stream_url': 'http://odna.octoshape.net/f3f5m2v4/cds/smil:ch5_auto.smil/playlist.m3u8'})
        self.plugin.add_list_item(data, is_folder=False)
        self.plugin.end_list()

    def action_play_stream(self):        
        self.plugin.set_stream_url(self.args['stream_url'])


    
##############
## EuroNews ##
##############

class EuroNews(BaseChannel):
    playable = False
    short_name = 'euronews'
    long_name = 'EuroNews'
    default_action = 'list_streams'
    
    def action_list_streams(self):
        data = {}
        data.update(self.args)
        data.update({'action': 'play_stream', 'Title': 'Arabic', 'stream_url': 'rtsp://fr-par-3.stream-relay.hexaglobe.net/rtpeuronewslive/ar_video750_rtp.sdp'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'English', 'stream_url': 'rtsp://fr-par-3.stream-relay.hexaglobe.net/rtpeuronewslive/en_video750_rtp.sdp'})
        self.plugin.add_list_item(data, is_folder=False)
	data.update({'action': 'play_stream', 'Title': 'French', 'stream_url': 'rtsp://fr-par-3.stream-relay.hexaglobe.net/rtpeuronewslive/fr_video750_rtp.sdp'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'German', 'stream_url': 'rtsp://fr-par-3.stream-relay.hexaglobe.net/rtpeuronewslive/de_video750_rtp.sdp'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Italian', 'stream_url': 'rtsp://fr-par-3.stream-relay.hexaglobe.net/rtpeuronewslive/it_video750_rtp.sdp'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Portuguese', 'stream_url': 'rtsp://fr-par-3.stream-relay.hexaglobe.net/rtpeuronewslive/pt_video750_rtp.sdp'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Russian', 'stream_url': 'rtsp://fr-par-3.stream-relay.hexaglobe.net/rtpeuronewslive/ru_video750_rtp.sdp'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Spanish', 'stream_url': 'rtsp://fr-par-3.stream-relay.hexaglobe.net/rtpeuronewslive/es_video750_rtp.sdp'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Turkish', 'stream_url': 'rtsp://fr-par-3.stream-relay.hexaglobe.net/rtpeuronewslive/tr_video750_rtp.sdp'})
        self.plugin.add_list_item(data, is_folder=False)
        self.plugin.end_list()

    def action_play_stream(self):        
        self.plugin.set_stream_url(self.args['stream_url'])

#############
## NASA TV ##
#############

class NASATV(BaseChannel):
    playable = False
    short_name = 'nasatv_en'
    long_name = 'NASA TV'
    default_action = 'list_streams'
	
    def action_list_streams(self):
        data = {}
        data.update(self.args)
        data.update({'action': 'play_stream', 'Title': 'NASA TV', 'stream_url': 'rtmp://infozen.fc.llnwd.net/infozen/ playpath=nasa_400 swfUrl=http://static.ls-cdn.com/player/5.10/livestation-player.swf swfVfy=1 live=1'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'NASA TV HD', 'stream_url': 'rtmp://infozen.fc.llnwd.net/infozen/ playpath=nasa_1000 swfUrl=http://static.ls-cdn.com/player/5.10/livestation-player.swf swfVfy=1 live=1'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'NASA Public Channel', 'stream_url': 'rtmp://ustreamlivefs.fplive.net/ustream2live-live/ playpath=stream_live_1_1_6540154 swfUrl=http://static-cdn1.ustream.tv/swf/live/viewer.rsl:96.swf swfVfy=1 live=1'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'NASA Media Channel', 'stream_url': 'rtmp://ustreamlivefs.fplive.net/ustream4live-live/ playpath=stream_live_1_1_10414700 swfUrl=http://static-cdn1.ustream.tv/swf/live/viewer.rsl:96.swf swfVfy=1 live=1'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'NASA Education Channel', 'stream_url': 'rtmp://infozen.fc.llnwd.net/infozen/edu_channel.flv'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'NASA Space Station Live', 'stream_url': 'rtmp://ustreamlivefs.fplive.net/ustream3live-live/ playpath=stream_live_1_1_9408562 swfUrl=http://static-cdn1.ustream.tv/swf/live/viewer.rsl:96.swf swfVfy=1 live=1'})
        self.plugin.add_list_item(data, is_folder=False)
        self.plugin.end_list()

    def action_play_stream(self):        
        self.plugin.set_stream_url(self.args['stream_url'])

#############
## Reuters ##
#############	

class REUTERS(BaseChannel):
    playable = True
    short_name = 'reuters'
    long_name = 'Reuters'
    default_action = 'play_stream'
    
    def action_play_stream(self):
	self.plugin.set_stream_url('http://37.58.85.156/rlo001/ngrp:rlo001.stream_all/playlist.m3u8')

########
## UT ##
########	

class UT(BaseChannel):
    playable = True
    short_name = 'ut'
    long_name = 'Ukraine Today'
    default_action = 'play_stream'
    
    def action_play_stream(self):
	self.plugin.set_stream_url('http://stream2g01-g50.1plus1.ua/380555/smil:380555.smil/playlist.m3u8')

################
## Rai News24 ##
################

class RAINEWS24(BaseChannel):
    playable = False
    short_name = 'rainews24'
    long_name = 'Rai News24 (Geo-restricted)'
    default_action = 'list_streams'
    
    def action_list_streams(self):
        data = {}
        data.update(self.args)
        data.update({'action': 'play_stream', 'Title': 'Medium Quality', 'stream_url': 'rtmp://rainews.lsops.net/live/ playpath=rainews_it_584 swfUrl="http://static.ls-cdn.com/player/5.10/livestation-player.swf" swfVfy=true live=true'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Mobile Quality', 'stream_url': 'http://rainews.lsops.net/live/rainews_it_hls.smil/playlist.m3u8'})
        self.plugin.add_list_item(data, is_folder=False)
        self.plugin.end_list()

    def action_play_stream(self):        
        self.plugin.set_stream_url(self.args['stream_url'])

#############
## PressTV ##
#############	

class PRESSTV(BaseChannel):
    playable = True
    short_name = 'press_tv'
    long_name = 'PressTV'
    default_action = 'play_stream'
    
    def action_play_stream(self):
	self.plugin.set_stream_url('http://media23.lsops.net/live/presstv_en_hls.smil/playlist.m3u8')

###############
## Bloomberg ##
###############

class BLOOMBERG(BaseChannel):
    playable = True
    short_name = 'bloomberg_en'
    long_name = 'Bloomberg Television'
    default_action = 'play_stream'
    
    def action_play_stream(self):        
        self.plugin.set_stream_url('http://live.bltvios.com.edgesuite.net/tv/us/master.m3u8')

####################################
## Channel NewsAsia International ##
####################################

class CNAI(BaseChannel):
    playable=True
    short_name = 'channel_newsasia'
    long_name = "Channel NewsAsia International (Geo-restricted)"
    default_action = 'play_stream'

    def action_play_stream(self):        
        self.plugin.set_stream_url('http://cna_hls-lh.akamaihd.net/i/cna_en@8000/master.m3u8')
	
##########
## eNCA ##
##########

class eNCA(BaseChannel):
    playable=True
    short_name = 'enca'
    long_name = "eNCA (South Africa)"
    default_action = 'play_stream'

    def action_play_stream(self):        
        self.plugin.set_stream_url('http://wpc.C1A9.edgecastcdn.net/hls-live/20C1A9/enca/ls_satlink/b_,264,528,828,.m3u8')

##############
## Sky News ##
##############

class SkyNews(BaseChannel):
    playable = False
    short_name = 'skynews'
    long_name = 'Sky News'
    default_action = 'list_streams'
    
    def action_list_streams(self):
        data = {}
        data.update(self.args)
        data.update({'action': 'play_stream', 'Title': 'Sky News', 'stream_url': 'http://ilg.club/streamlink.m3u8?channel_id=31b003ab7e7749a798fe00424e3dd9ff&bitrate=800'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Sky News HD', 'stream_url': 'plugin://plugin.video.youtube/?action=play_video&videoid=VYlQJbsVs48'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Sky News International', 'stream_url': 'http://wpc.C1A9.edgecastcdn.net/hls-live/20C1A9/skynews/ls_satlink/b_,264,528,828,.m3u8'})
        self.plugin.add_list_item(data, is_folder=False)
        self.plugin.end_list()

    def action_play_stream(self):        
        self.plugin.set_stream_url(self.args['stream_url'])

##############
## France24 ##
##############

class France24(BaseChannel):
    playable = False
    short_name = 'france24'
    long_name = 'France 24'
    default_action = 'list_streams'
    
    def action_list_streams(self):
        data = {}
        data.update(self.args)
        data.update({'action': 'play_stream', 'Title': 'English', 'stream_url': 'http://vipwowza.yacast.net/f24_hlslive_en/smil:iphone.fr24en.smil/playlist.m3u8'})
        self.plugin.add_list_item(data, is_folder=False)
        self.plugin.end_list()

    def action_play_stream(self):        
        self.plugin.set_stream_url(self.args['stream_url'])
    
####################
## Deutsche Welle ##
####################    

class DW(BaseChannel):
    playable = False
    short_name = 'dw'
    long_name = 'Deutsche Welle (DW)'
    default_action = 'list_streams'
    
    def action_list_streams(self):
        data = {}
        data.update(self.args)
        data.update({'action': 'play_stream', 'Title': 'DW (Asia)', 'stream_url': 'http://www.metafilegenerator.de/DWelle/tv-asia/ios/master.m3u8'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'DW (Europe)', 'stream_url': 'http://www.metafilegenerator.de/DWelle/tv-europa/ios/master.m3u8'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'DW (Latinoamerica)', 'stream_url': 'http://www.metafilegenerator.de/DWelle/tv-latinoamerica/ios/master.m3u8'})
        self.plugin.add_list_item(data, is_folder=False)
        self.plugin.end_list()

    def action_play_stream(self):        
        self.plugin.set_stream_url(self.args['stream_url'])
        
#################
## VoA Persian ##
#################

class VoAPersian(BaseChannel):
    playable = False
    short_name = 'voapersian'
    long_name = 'VoA Persian'
    default_action = 'list_streams'
    
    def action_list_streams(self):
        data = {}
        data.update(self.args)
        data.update({'action': 'play_stream', 'Title': 'Medium Quality', 'stream_url': 'rtmp://hd4.lsops.net/live playpath=voiceofa_fa_485 swfUrl="http://static.ls-cdn.com/player/5.10/livestation-player.swf" swfVfy=true live=true'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Low Quality', 'stream_url': 'rtmp://hd4.lsops.net/live playpath=voiceofa_fa_183 swfUrl="http://static.ls-cdn.com/player/5.10/livestation-player.swf" swfVfy=true live=true'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Mobile Quality', 'stream_url': 'http://hd4.lsops.net/live/voiceofa_fa_hls.smil/playlist.m3u8'})
        self.plugin.add_list_item(data, is_folder=False)
        self.plugin.end_list()

    def action_play_stream(self):        
        self.plugin.set_stream_url(self.args['stream_url'])

########################
## The People's Voice ##
########################    

class TPV(BaseChannel):
    playable = False
    short_name = 'tpv'
    long_name = 'The People`s Voice'
    default_action = 'list_streams'
    
    def action_list_streams(self):
        data = {}
        data.update(self.args)
        data.update({'action': 'play_stream', 'Title': 'High Quality', 'stream_url': 'rtmp://cdn.rbm.tv/rightbrainmedia-live-106/_definst_/ddstream_3'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Mobile Quality', 'stream_url': 'http://cdn.rbm.tv:1935/rightbrainmedia-live-106/_definst_/ddstream_3/playlist.m3u8'})
        self.plugin.add_list_item(data, is_folder=False)
        self.plugin.end_list()

    def action_play_stream(self):        
        self.plugin.set_stream_url(self.args['stream_url'])
        
###############
## NHK WORLD ##
###############

class NHK(BaseChannel):
    playable = True
    short_name = 'nhk_world'
    long_name = 'NHK World TV'
    default_action = 'play_stream' 

    def action_play_stream(self):
        self.plugin.set_stream_url('http://plslive-w.nhk.or.jp/nhkworld/app/live.m3u8')
        
###############
## CCTV News ##
###############

#class CCTV(BaseChannel):
#    playable = True
#    short_name = 'cctv_news_english'
#    long_name = 'CCTV News'
#    default_action = 'play_stream' 

#    def action_play_stream(self):
#        self.plugin.set_stream_url('http://88.212.11.206:5000/live/22/22.m3u8')   

#########
## CNN ##
#########

class CNN(BaseChannel):
    playable = False
    short_name = 'cnn'
    long_name = 'CNN International'
    default_action = 'list_streams'
    
    def action_list_streams(self):
        data = {}
        data.update(self.args)
        data['action'] = 'play_stream'
        data.update({'stream_url': "http://hls.novotelecom.ru/streaming/cnn/tvrec/playlist.m3u8", 'Title': 'High Quality'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'stream_url': "http://cnn-hls.live.numericable.tv/live/hls/cnn/ipad.m3u8", 'Title': 'Medium Quality'})
        self.plugin.add_list_item(data, is_folder=False)
        self.plugin.end_list()

    def action_play_stream(self):        
        self.plugin.set_stream_url(self.args['stream_url'])

##############
## 24 Vesti ##
##############

class VESTI(BaseChannel):
    playable = True
    short_name = '24vesti'
    long_name = '24 Vesti'
    default_action = 'play_stream'
    
    def action_play_stream(self):
	self.plugin.set_stream_url('mms://62.162.58.55/24vesti')
	
###############
## NDTV 24x7 ##
###############

class NDTV(BaseChannel):
    playable = True
    short_name = 'ndtv_24x7'
    long_name = 'NDTV 24x7'
    default_action = 'play_stream' 

    def action_play_stream(self):
        self.plugin.set_stream_url('rtmp://ndtv.lsops.net/live/ playpath=ndtv_en_364 swfUrl=http://static.ls-cdn.com/player/5.10/livestation-player.swf swfVfy=1 live=1')
