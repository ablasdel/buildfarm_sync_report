buildfarm_sync_report
=====================

To use this script execute the following:

python syncdiff.py *beforefile* *afterfile*

What follows is an example output for syncdiff run on the following files: (if viewing in github view in raw for real results)

http://packages.ros.org/ros/ubuntu/dists/precise/main/binary-amd64/Packages

http://packages.ros.org/ros-shadow-fixed/ubuntu/dists/precise/main/binary-amd64/Packages


Packages Added: 
ros-fuerte-applanix-driver : 0.1.0-s1360394766~precise
ros-fuerte-extremum-seeking : 0.1.0-s1359882697~precise
ros-fuerte-humanoid-navigation : 0.4.0-s1360626045~precise
ros-fuerte-husky-apps : 0.1.0-s1360569064~precise
ros-fuerte-husky-desktop : 1.0.0-s1360714896~precise
ros-fuerte-husky-robot : 1.0.0-s1360714896~precise
ros-fuerte-husky-simulator : 0.1.0-s1360569645~precise
ros-fuerte-object-recognition-renderer : 0.1.8-0precise-20130207-2247-+0000
ros-fuerte-object-recognition-tabletop : 0.2.17-0precise-20130211-2333-+0000
ros-fuerte-rms-pr2-gazebo-environment : 0.1.0-s1360629415~precise
ros-fuerte-saliency-detection : 0.1.2-s1360280633~precise
ros-fuerte-shared-serial : 0.1.0-s1359883977~precise
ros-fuerte-speakeasy : 0.1.1-s1360621923~precise
ros-fuerte-sr-ronex : 0.9.0.2-s1360634239~precise
ros-fuerte-velo-gripper : 0.1.0-s1360623334~precise
ros-fuerte-webmap : 0.1.0-s1359905473~precise
ros-groovy-cmd-vel-mux : 0.2.2-0precise-20130209-1836-+0000
ros-groovy-kobuki-arm : 0.3.4-0precise-20130211-0912-+0000
ros-groovy-kobuki-auto-docking : 0.3.4-0precise-20130210-1050-+0000
ros-groovy-kobuki-bumper2pc : 0.3.4-0precise-20130210-1102-+0000
ros-groovy-kobuki-controller-tutorial : 0.3.4-0precise-20130210-1103-+0000
ros-groovy-kobuki-driver : 0.3.4-0precise-20130210-1059-+0000
ros-groovy-kobuki-ftdi : 0.3.4-0precise-20130210-1104-+0000
ros-groovy-kobuki-keyop : 0.3.4-0precise-20130210-1109-+0000
ros-groovy-kobuki-node : 0.3.4-0precise-20130211-0446-+0000
ros-groovy-kobuki-safety-controller : 0.3.4-0precise-20130210-1111-+0000
ros-groovy-kobuki-testsuite : 0.3.4-0precise-20130211-0734-+0000
ros-groovy-yocs-controllers : 0.2.2-0precise-20130209-1835-+0000
ros-groovy-yocs-velocity-smoother : 0.2.2-0precise-20130209-1833-+0000

Packages Removed: 
ros-fuerte-care-o-bot : 1.0.0-s1356669545~precise
ros-fuerte-care-o-bot-desktop : 1.0.0-s1356669545~precise
ros-fuerte-care-o-bot-robot : 1.0.0-s1356669545~precise
ros-fuerte-clearpath-husky-robot : 1.0.0-s1356669545~precise
ros-fuerte-cob-robots : 0.4.6-s1356649489~precise
ros-fuerte-cob-simulation : 0.4.5-s1356650766~precise
ros-fuerte-moveit-core : 0.1.4-0precise-20121011-1050-+0000
ros-fuerte-openrtm : 1.1.0-s1348523615~precise
ros-fuerte-rocon-comms : 0.1.1-s1352271385~precise
ros-fuerte-rocon-msgs : 0.1.4-s1356245210~precise
ros-fuerte-rocon-multimaster : 0.1.9-s1356505850~precise
ros-fuerte-schunk-modular-robotics : 0.4.4-s1356573569~precise
ros-fuerte-schunk-robots : 0.1.2-s1356580849~precise
ros-fuerte-schunk-simulation : 0.1.2-s1356650606~precise
ros-fuerte-zeroconf-comms : 0.1.6-s1352269974~precise
ros-fuerte-zeroconf-implementations : 0.1.6-s1347128628~precise
ros-groovy-kobuki-desktop : 0.1.3-s1360129864~precise
ros-groovy-turtlebot : 1.9.4-s1360121565~precise
ros-groovy-turtlebot-apps : 1.9.2-s1360294453~precise
ros-groovy-turtlebot-dashboard : 0.1.0-s1360093140~precise
ros-groovy-turtlebot-viz : 1.9.3-s1360275015~precise

Packages Updated: 
ros-fuerte-abb : 0.1.1-s1355476312~precise -> 0.1.1-s1360623739~precise
ros-fuerte-ackermann-msgs : 0.4.0-s1347128650~precise -> 0.4.0-s1359882625~precise
ros-fuerte-actionlib : 1.8.7-0precise-20120908-1822-+0000 -> 1.8.7-0precise-20130211-0914-+0000
ros-fuerte-adept : 0.1.0-s1356581194~precise -> 0.1.0-s1360669724~precise
ros-fuerte-ar-track-alvar : 0.3.0-s1350942569~precise -> 0.3.0-s1360281017~precise
ros-fuerte-arbotix : 0.6.1-s1347138065~precise -> 0.6.1-s1360621183~precise
ros-fuerte-arm-navigation : 1.1.11-s1355471857~precise -> 1.1.11-s1360583056~precise
ros-fuerte-arm-navigation-experimental : 0.5.7-s1356573583~precise -> 0.5.7-s1360631575~precise
ros-fuerte-art-vehicle : 0.4.3-s1354952807~precise -> 0.4.3-s1360399713~precise
ros-fuerte-audio-common : 0.1.9-s1348595008~precise -> 0.1.9-s1360621162~precise
ros-fuerte-axis-camera : 0.0.1-s1351634191~precise -> 0.0.1-s1359882591~precise
ros-fuerte-bfl : 0.1.0-s1347124244~precise -> 0.1.0-s1359841319~precise
ros-fuerte-bond-core : 1.6.3-s1347128144~precise -> 1.6.3-s1359882803~precise
ros-fuerte-bosch-3rdparty : 0.1.1-s1347122886~precise -> 0.1.1-s1359838743~precise
ros-fuerte-bosch-common : 0.1.1-s1349902568~precise -> 0.1.1-s1360280767~precise
ros-fuerte-bosch-drivers : 0.4.2-s1349902615~precise -> 0.4.2-s1360280818~precise
ros-fuerte-bosch-image-proc : 0.2.1-s1349902405~precise -> 0.2.1-s1360280722~precise
ros-fuerte-bosch-proximity-sensor : 1.0.0-s1349906468~precise -> 1.0.0-s1360282973~precise
ros-fuerte-bosch-web-visualization : 0.5.0-s1352981035~precise -> 0.5.0-s1360283759~precise
ros-fuerte-brown-drivers : 0.0.9-s1347133999~precise -> 0.0.9-s1359887628~precise
ros-fuerte-brown-perception : 0.0.10-s1347138247~precise -> 0.0.10-s1359961420~precise
ros-fuerte-brown-remotelab : 0.1.1-s1347171400~precise -> 0.1.1-s1360025507~precise
ros-fuerte-bullet : 2.79-s1347124289~precise -> 2.79-s1359841903~precise
ros-fuerte-calibration : 0.9.6-s1349906374~precise -> 0.9.6-s1360621441~precise
ros-fuerte-camera-drivers : 1.8.0-s1347170068~precise -> 1.8.0-s1359908078~precise
ros-fuerte-camera-info-manager-py : 0.1.0-s1354777852~precise -> 0.1.0-s1359882672~precise
ros-fuerte-camera-pose : 0.5.0-s1356580301~precise -> 0.5.0-s1360645189~precise
ros-fuerte-camera-umd : 0.1.5-s1347169443~precise -> 0.1.5-s1359905526~precise
ros-fuerte-camera1394 : 1.8.0-s1347169360~precise -> 1.8.0-s1359905698~precise
ros-fuerte-catkin : 0.4.5-0precise-20120908-1619-+0000 -> 0.4.5-0precise-20130202-0920-+0000
ros-fuerte-clearpath-common : 0.2.5-s1354560628~precise -> 0.2.5-s1359965440~precise
ros-fuerte-clearpath-husky : 0.3.1-s1356649111~precise -> 0.3.2-s1360629280~precise
ros-fuerte-clearpath-kinect : 0.2.1-s1354561990~precise -> 0.2.1-s1360023149~precise
ros-fuerte-clearpath-turtlebot : 0.2.0-s1356649731~precise -> 0.2.0-s1360403739~precise
ros-fuerte-client-rosjava-jni : 0.1.9-s1347134030~precise -> 0.1.9-s1359887740~precise
ros-fuerte-cob-calibration-data : 0.1.1-s1347122839~precise -> 0.1.2-s1359839610~precise
ros-fuerte-cob-command-tools : 0.4.4-s1356578469~precise -> 0.4.6-s1360638333~precise
ros-fuerte-cob-common : 0.4.5-s1347139583~precise -> 0.4.6-s1360028431~precise
ros-fuerte-cob-driver : 0.4.10-s1360634030~precise -> 0.4.8-s1356573707~precise
ros-fuerte-cob-environments : 0.4.3-s1347175111~precise -> 0.4.4-s1360032245~precise
ros-fuerte-cob-extern : 0.4.2-s1347122834~precise -> 0.4.3-s1359838827~precise
ros-fuerte-cob-navigation : 0.4.2-s1350952116~precise -> 0.4.2-s1360629619~precise
ros-fuerte-cob-perception-common : 0.1.0-s1349902669~precise -> 0.1.0-s1360281019~precise
ros-fuerte-cob-substitute : 0.1.1-s1356573688~precise -> 0.1.1-s1360658101~precise
ros-fuerte-common : 1.8.0-s1347133548~precise -> 1.8.0-s1360583308~precise
ros-fuerte-common-msgs : 1.8.13-0precise-20120908-1740-+0000 -> 1.8.13-0precise-20130203-0848-+0000
ros-fuerte-common-rosdeps : 1.2.0-s1347122840~precise -> 1.2.0-s1359838704~precise
ros-fuerte-common-tutorials : 0.2.3-s1348603925~precise -> 0.2.3-s1360583368~precise
ros-fuerte-console-bridge : 0.1.2-0precise-20120908-1622-+0000 -> 0.1.2-6precise-20130204-2237-+0000
ros-fuerte-continuous-ops : 0.4.3-s1356578794~precise -> 0.4.3-s1360638952~precise
ros-fuerte-control : 1.0.1-s1347128138~precise -> 1.0.1-s1359882675~precise
ros-fuerte-cram-core : 0.1.8-s1348595682~precise -> 0.1.8-s1359888826~precise
ros-fuerte-desktop : 1.0.0-s1355574845~precise -> 1.0.0-s1360714896~precise
ros-fuerte-desktop-full : 1.0.0-s1355574845~precise -> 1.0.0-s1360714896~precise
ros-fuerte-diagnostics : 1.6.4-s1347133484~precise -> 1.6.4-s1359887663~precise
ros-fuerte-diagnostics-monitors : 1.4.3-s1352877673~precise -> 1.4.3-s1360014453~precise
ros-fuerte-dmp : 0.3.0-s1350941835~precise -> 0.3.0-s1359893870~precise
ros-fuerte-documentation : 1.5.3-s1347128195~precise -> 1.5.3-s1359882622~precise
ros-fuerte-driver-common : 1.4.0-s1347168681~precise -> 1.4.0-s1359893667~precise
ros-fuerte-dynamic-reconfigure : 1.4.2-s1347168414~precise -> 1.4.2-s1359882774~precise
ros-fuerte-dynamixel-motor : 0.2.3-s1351635940~precise -> 0.2.3-s1360582760~precise
ros-fuerte-ecl-core : 0.44.0-s1352272514~precise -> 0.44.0-s1359905760~precise
ros-fuerte-ecl-lite : 0.44.0-s1352271694~precise -> 0.44.0-s1359893320~precise
ros-fuerte-ecl-manipulation : 0.44.0-s1352274179~precise -> 0.44.0-s1359909647~precise
ros-fuerte-ecl-navigation : 0.44.0-s1352273997~precise -> 0.44.0-s1359909030~precise
ros-fuerte-ecl-tools : 0.44.0-s1352270259~precise -> 0.44.0-s1359887348~precise
ros-fuerte-ecto : 0.4.16-0precise-20121109-0604-+0000 -> 0.5.3-0precise-20130202-0927-+0000
ros-fuerte-ecto-image-pipeline : 0.4.7-0precise-20121130-0042-+0000 -> 0.4.8-0precise-20130207-2308-+0000
ros-fuerte-ecto-opencv : 0.4.17-0precise-20121129-2156-+0000 -> 0.4.21-0precise-20130207-2253-+0000
ros-fuerte-ecto-openni : 0.3.7-0precise-20121109-0630-+0000 -> 0.3.8-0precise-20130207-2249-+0000
ros-fuerte-ecto-pcl : 0.3.9-0precise-20121118-2356-+0000 -> 0.3.9-0precise-20130207-2321-+0000
ros-fuerte-ecto-ros : 0.3.21-0precise-20121118-2332-+0000 -> 0.3.23-0precise-20130207-2246-+0000
ros-fuerte-erratic-robot : 0.3.1-s1356575369~precise -> 0.3.1-s1360629309~precise
ros-fuerte-ethzasl-aseba : 1.0.0-s1349140427~precise -> 1.0.0-s1360621613~precise
ros-fuerte-ethzasl-icp-mapping : 0.9.0-s1355968904~precise -> 0.9.5-s1360621311~precise
ros-fuerte-ethzasl-message-transport : 0.8.2-s1354951710~precise -> 0.8.3-s1360399815~precise
ros-fuerte-ethzasl-xsens-driver : 1.0.1-s1347133577~precise -> 1.0.1-s1359887898~precise
ros-fuerte-executive-smach : 1.2.0-s1347133680~precise -> 1.2.0-s1360582958~precise
ros-fuerte-executive-smach-visualization : 1.0.2-s1352876983~precise -> 1.0.2-s1360619618~precise
ros-fuerte-executive-teer : 1.0.0-s1348603770~precise -> 1.0.0-s1360368246~precise
ros-fuerte-exploration : 0.4.1-s1350952171~precise -> 0.4.1-s1360629160~precise
ros-fuerte-fcl : 0.2.3-0precise-20121011-1035-+0000 -> 0.2.3-0precise-20130211-0920-+0000
ros-fuerte-filters : 1.6.0-s1347133504~precise -> 1.6.0-s1359887745~precise
ros-fuerte-flann : 1.7.1-1precise-20130203-1637-+0000 -> 1.7.1-8precise-20120813-1214-+0000
ros-fuerte-flirtlib : 0.1.4-0precise-20120908-1622-+0000 -> 0.1.5-0precise-20130202-0924-+0000
ros-fuerte-freenect-stack : 0.1.0-s1355812663~precise -> 0.1.1-s1360283368~precise
ros-fuerte-freiburg-tools : 0.2.0-s1356650558~precise -> 0.2.0-s1360629174~precise
ros-fuerte-gencpp : 0.3.4-0precise-20120908-1637-+0000 -> 0.3.4-0precise-20130202-2203-+0000
ros-fuerte-genlisp : 0.3.3-0precise-20120908-1637-+0000 -> 0.3.3-0precise-20130202-2203-+0000
ros-fuerte-genmsg : 0.3.10-0precise-20120908-1622-+0000 -> 0.3.10-0precise-20130202-2131-+0000
ros-fuerte-genpy : 0.3.7-0precise-20120908-1638-+0000 -> 0.3.7-0precise-20130202-2203-+0000
ros-fuerte-geographic-info : 0.2.1-s1347133668~precise -> 0.2.1-s1359888186~precise
ros-fuerte-geometry : 1.8.2-s1347128281~precise -> 1.8.2-s1359882841~precise
ros-fuerte-geometry-experimental : 0.2.3-s1347133731~precise -> 0.2.3-s1360583192~precise
ros-fuerte-geometry-tutorials : 0.1.3-s1348603799~precise -> 0.1.3-s1360368353~precise
ros-fuerte-geometry-visualization : 0.1.1-s1352876864~precise -> 0.1.1-s1360620486~precise
ros-fuerte-gps-drivers : 0.2.0-s1347133572~precise -> 0.2.0-s1359888816~precise
ros-fuerte-gps-umd : 0.1.5-s1347128230~precise -> 0.1.5-s1359882777~precise
ros-fuerte-graspit-simulator : 0.4.0-s1356579480~precise -> 0.4.0-s1360663148~precise
ros-fuerte-hector-common : 0.1.1-s1349140478~precise -> 0.1.1-s1359887444~precise
ros-fuerte-hector-gazebo : 0.1.1-s1349140895~precise -> 0.1.2-s1360307653~precise
ros-fuerte-hector-models : 0.1.0-s1347122849~precise -> 0.1.1-s1360307625~precise
ros-fuerte-hector-quadrotor : 0.1.1-s1349141458~precise -> 0.1.1-s1360311143~precise
ros-fuerte-hector-quadrotor-apps : 0.1.1-s1351102238~precise -> 0.1.1-s1360314351~precise
ros-fuerte-hector-slam : 0.1.1-s1350944910~precise -> 0.2.2-s1360280869~precise
ros-fuerte-hector-worldmodel : 0.2.0-s1354237065~precise -> 0.2.0-s1360282565~precise
ros-fuerte-humanoid-msgs : 0.1.1.1-s1347128139~precise -> 0.1.2-s1359882971~precise
ros-fuerte-humanoid-walk : 0.2.0-s1347141728~precise -> 0.2.0-s1359893831~precise
ros-fuerte-ias-common : 0.1.3-s1355476546~precise -> 0.1.3-s1360623466~precise
ros-fuerte-image-common : 1.8.0-s1347133482~precise -> 1.8.0-s1359887789~precise
ros-fuerte-image-pipeline : 1.8.5-s1349902794~precise -> 1.8.5-s1360281094~precise
ros-fuerte-image-transport-plugins : 1.8.5-s1354950170~precise -> 1.8.6-s1360395108~precise
ros-fuerte-imu-drivers : 1.4.0-s1347141984~precise -> 1.4.0-s1359893561~precise
ros-fuerte-industrial : 0.2.0-s1356579445~precise -> 0.2.0-s1360663091~precise
ros-fuerte-industrial-desktop : 1.0.0-s1356669545~precise -> 1.0.0-s1360714896~precise
ros-fuerte-joystick-drivers : 1.8.1-s1351633928~precise -> 1.8.2-s1359962653~precise
ros-fuerte-joystick-drivers-tutorials : 1.6.0-s1351660740~precise -> 1.6.0-s1360368263~precise
ros-fuerte-keyboardteleopjs : 0.1.1-s1351636295~precise -> 0.1.1-s1359838863~precise
ros-fuerte-kingfisher : 0.1.1-s1354951782~precise -> 0.1.2-s1360399682~precise
ros-fuerte-kingfisher-apps : 0.1.0-s1351662269~precise -> 0.1.0-s1359965224~precise
ros-fuerte-kingfisher-desktop : 1.0.0-s1355574845~precise -> 1.0.0-s1360714896~precise
ros-fuerte-kingfisher-robot : 1.0.0-s1355574845~precise -> 1.0.0-s1360714896~precise
ros-fuerte-knowrob : 0.2.2-s1355479978~precise -> 0.2.2-s1360629794~precise
ros-fuerte-kobuki-msgs : 0.1.6-s1356245286~precise -> 0.1.6-s1359882776~precise
ros-fuerte-langs : 0.3.5-0precise-20120908-1707-+0000 -> 0.3.5-0precise-20130203-0630-+0000
ros-fuerte-langs-dev : 0.1.3-0precise-20120908-1646-+0000 -> 0.1.3-0precise-20130202-2209-+0000
ros-fuerte-laser-drivers : 1.6.0-s1347169125~precise -> 1.6.0-s1359905117~precise
ros-fuerte-laser-pipeline : 1.4.5-s1350943746~precise -> 1.4.5-s1360023279~precise
ros-fuerte-lfd : 0.1.0-s1352976965~precise -> 0.1.0-s1359883233~precise
ros-fuerte-libccd : 1.4.0-0precise-20120813-1203-+0000 -> 1.4.0-0precise-20130202-2031-+0000
ros-fuerte-libg2o : 2012.11.09-0precise-20121109-0201-+0000 -> 2012.11.09-0precise-20130202-0927-+0000
ros-fuerte-librms : 0.0.1-s1352977556~precise -> 0.2.0-s1359882901~precise
ros-fuerte-linux-networking : 0.1.17-s1354845017~precise -> 0.1.17-s1360619575~precise
ros-fuerte-map-manager-app : 0.1.1-s1348598774~precise -> 0.1.1-s1359905794~precise
ros-fuerte-map-msgs : 0.0.1-s1355957722~precise -> 0.0.1-s1359882853~precise
ros-fuerte-map-store : 0.1.0-s1348598000~precise -> 0.1.0-s1359894469~precise
ros-fuerte-map2djs : 0.1.0-s1351634898~precise -> 0.1.0-s1359838896~precise
ros-fuerte-megatree : 0.1.8-s1347122892~precise -> 0.1.8-s1359839145~precise
ros-fuerte-megatree-pcl : 0.1.1-s1347171420~precise -> 0.1.1-s1360023128~precise
ros-fuerte-mjpeg-server : 1.0.1-s1349902866~precise -> 1.0.1-s1360281321~precise
ros-fuerte-mjpegcanvasjs : 0.1.0-s1351635402~precise -> 0.1.0-s1359839041~precise
ros-fuerte-mobile : 1.0.0-s1350987161~precise -> 1.0.0-s1360714896~precise
ros-fuerte-motion-analysis-mocap : 0.2.1-s1347133828~precise -> 0.2.1-s1359887393~precise
ros-fuerte-motoman : 0.1.1-s1356581457~precise -> 0.1.1-s1360666442~precise
ros-fuerte-move-arm : 1.0.0-s1356669545~precise -> 1.0.0-s1360714896~precise
ros-fuerte-moveit-msgs : 0.2.7-0precise-20120925-0833-+0000 -> 0.2.8-0precise-20130211-1309-+0000
ros-fuerte-multimaster-experimental : 0.2.1-s1347128250~precise -> 0.2.1-s1359883181~precise
ros-fuerte-nasa-r2-common : 0.0.4-s1355472001~precise -> 0.0.4-s1360029863~precise
ros-fuerte-nasa-r2-simulator : 0.0.7-s1356575601~precise -> 0.0.7-s1360629619~precise
ros-fuerte-nav2djs : 0.1.1-s1351634507~precise -> 0.1.1-s1359839338~precise
ros-fuerte-navigation : 1.8.3-s1350945002~precise -> 1.8.3-s1360583200~precise
ros-fuerte-navigation-experimental : 0.1.10-s1356573442~precise -> 0.1.10-s1360622418~precise
ros-fuerte-navigation-tutorials : 0.1.1-s1350952571~precise -> 0.1.1-s1360629337~precise
ros-fuerte-netft : 0.1.3-s1356573535~precise -> 0.1.3-s1359910069~precise
ros-fuerte-nmea-gps-driver : 0.2.0-s1347128224~precise -> 0.2.0-s1359883476~precise
ros-fuerte-nodelet-core : 1.6.5-s1347168835~precise -> 1.6.5-s1359894314~precise
ros-fuerte-object-manipulation : 0.6.8-s1356575710~precise -> 0.6.9-s1360658093~precise
ros-fuerte-object-recognition-capture : 0.2.15-0precise-20121130-0211-+0000 -> 0.2.18-0precise-20130207-2330-+0000
ros-fuerte-object-recognition-core : 0.4.11-0precise-20121130-0120-+0000 -> 0.4.18-0precise-20130207-2319-+0000
ros-fuerte-object-recognition-linemod : 0.2.5-0precise-20121130-0210-+0000 -> 0.2.9-0precise-20130207-2335-+0000
ros-fuerte-object-recognition-msgs : 0.3.11-0precise-20121119-0111-+0000 -> 0.3.13-0precise-20130207-2313-+0000
ros-fuerte-object-recognition-reconstruction : 0.2.15-0precise-20121130-0213-+0000 -> 0.2.20-0precise-20130207-2333-+0000
ros-fuerte-object-recognition-ros : 0.1.13-0precise-20130211-1148-+0000 -> 0.1.5-0precise-20121130-0212-+0000
ros-fuerte-object-recognition-tod : 0.4.12-0precise-20130207-2342-+0000 -> 0.4.9-0precise-20121130-0208-+0000
ros-fuerte-object-recognition-transparent-objects : 0.3.12-0precise-20130207-2337-+0000 -> 0.3.8-0precise-20121130-0210-+0000
ros-fuerte-occupancy-grid-utils : 0.5.1-s1350948036~precise -> 0.5.1-s1360620950~precise
ros-fuerte-octomap-mapping : 0.4.5-s1355476441~precise -> 0.4.6-s1360625824~precise
ros-fuerte-octomap-msgs : 0.1.4-0precise-20120908-1810-+0000 -> 0.1.4-0precise-20130211-0930-+0000
ros-fuerte-octomap-ros : 0.1.1-s1349958340~precise -> 0.1.1-s1360588363~precise
ros-fuerte-octovis : 1.4.2-0precise-20130202-0656-+0000 -> 1.4.2-4precise-20121011-1032-+0000
ros-fuerte-ompl : 0.11.1002045-0precise-20120908-1622-+0000 -> 0.11.1002045-0precise-20130202-2026-+0000
ros-fuerte-opencv-candidate : 0.1.3-0precise-20121109-0542-+0000 -> 0.1.8-0precise-20130207-2246-+0000
ros-fuerte-opencv2 : 2.4.2-0precise-20120908-1624-+0000 -> 2.4.2-1precise-20130207-2229-+0000
ros-fuerte-openni-camera : 1.8.6-s1356582062~precise -> 1.8.6-s1359905615~precise
ros-fuerte-openni-kinect : 0.5.2-s1356648587~precise -> 0.5.2-s1360284993~precise
ros-fuerte-openni-launch : 1.8.3-s1356583165~precise -> 1.8.3-s1360283342~precise
ros-fuerte-openni-tracker : 0.1.3-s1356648070~precise -> 0.1.3-s1359887887~precise
ros-fuerte-orocos-kinematics-dynamics : 0.2.3-s1347124102~precise -> 0.2.3-s1359841531~precise
ros-fuerte-orocos-toolchain : 2.6.0-3-s1356245522~precise -> 2.6.0.5-s1359841551~precise
ros-fuerte-pcl : 1.5.2-7precise-20120908-1813-+0000 -> 1.5.2-9precise-20130204-2056-+0000
ros-fuerte-people : 0.1.4-s1349906454~precise -> 0.1.4-s1360621957~precise
ros-fuerte-perception : 1.0.0-s1355574845~precise -> 1.0.0-s1360714896~precise
ros-fuerte-perception-pcl : 1.2.3-s1347170256~precise -> 1.2.3-s1360020442~precise
ros-fuerte-perception-pcl-fuerte-unstable : 0.3-s1347174341~precise -> 0.3-s1359905666~precise
ros-fuerte-physics-ode : 1.8.0-s1347122907~precise -> 1.8.0-s1359839405~precise
ros-fuerte-pluginlib : 1.8.0-s1347128156~precise -> 1.8.0-s1359883047~precise
ros-fuerte-pr2 : 1.0.0-s1356669545~precise -> 1.0.0-s1360714896~precise
ros-fuerte-pr2-applications : 1.0.0-s1356669545~precise -> 1.0.0-s1360714896~precise
ros-fuerte-pr2-apps : 0.4.6-s1356575770~precise -> 0.5.0-s1360634566~precise
ros-fuerte-pr2-arm-navigation : 0.5.2-s1356575716~precise -> 0.5.2-s1360635191~precise
ros-fuerte-pr2-assisted-teleop-app : 0.1.1-s1356578086~precise -> 0.1.1-s1360638162~precise
ros-fuerte-pr2-base : 1.0.0-s1356669545~precise -> 1.0.0-s1360714896~precise
ros-fuerte-pr2-calibration : 1.3.0-s1356578367~precise -> 1.3.0-s1360638435~precise
ros-fuerte-pr2-common : 1.8.2-s1347141170~precise -> 1.8.2-s1359894518~precise
ros-fuerte-pr2-common-actions : 0.4.0-s1356573677~precise -> 0.4.0-s1360629684~precise
ros-fuerte-pr2-controllers : 1.8.1-s1356572075~precise -> 1.8.1-s1360583520~precise
ros-fuerte-pr2-desktop : 1.0.0-s1356669545~precise -> 1.0.0-s1360714896~precise
ros-fuerte-pr2-ethercat-drivers : 1.7.1-s1356572207~precise -> 1.7.1-s1359908370~precise
ros-fuerte-pr2-exploration : 0.4.1-s1356580056~precise -> 0.4.1-s1360646321~precise
ros-fuerte-pr2-gui : 1.0.4-s1352880393~precise -> 1.0.4-s1360015042~precise
ros-fuerte-pr2-hardware : 0.0.1-s1356586383~precise -> 0.0.1-s1359908230~precise
ros-fuerte-pr2-interactive-manipulation : 1.0.0-s1356669545~precise -> 1.0.0-s1360714896~precise
ros-fuerte-pr2-kinematics : 0.4.4-s1355476290~precise -> 0.4.4-s1360623397~precise
ros-fuerte-pr2-make-a-map-app : 0.1.0-s1356578406~precise -> 0.1.0-s1360638317~precise
ros-fuerte-pr2-mannequin-mode-app : 0.1.0-s1356578350~precise -> 0.1.0-s1360638391~precise
ros-fuerte-pr2-map-navigation-app : 0.1.1-s1356580200~precise -> 0.1.1-s1360644921~precise
ros-fuerte-pr2-mechanism : 1.6.4-s1356571098~precise -> 1.6.4-s1359906198~precise
ros-fuerte-pr2-navigation : 0.1.13-s1356578055~precise -> 0.1.13-s1360638327~precise
ros-fuerte-pr2-navigation-apps : 0.1.1-s1356580240~precise -> 0.1.1-s1360645040~precise
ros-fuerte-pr2-object-manipulation : 0.6.6-s1356579539~precise -> 0.6.7-s1360663130~precise
ros-fuerte-pr2-pan-tilt : 0.1.0-s1356573477~precise -> 0.1.0-s1360622379~precise
ros-fuerte-pr2-plugs : 0.6.3-s1356575899~precise -> 0.6.3-s1360634476~precise
ros-fuerte-pr2-power-drivers : 1.0.9-s1347168957~precise -> 1.0.9-s1359906248~precise
ros-fuerte-pr2-props-app : 0.1.0-s1356584428~precise -> 0.1.0-s1360682015~precise
ros-fuerte-pr2-props-stack : 0.1.0-s1356583133~precise -> 0.1.0-s1360669012~precise
ros-fuerte-pr2-ps3-joystick-app : 0.1.0-s1356578383~precise -> 0.1.0-s1360638444~precise
ros-fuerte-pr2-robot : 1.4.0-s1356573645~precise -> 1.4.0-s1360628992~precise
ros-fuerte-pr2-self-test : 0.4.0-s1356578202~precise -> 0.4.0-s1360638043~precise
ros-fuerte-pr2-simulator : 1.8.6-s1356573626~precise -> 1.8.6-s1360622464~precise
ros-fuerte-pr2-teleop-app : 0.1.0-s1356578622~precise -> 0.1.0-s1360638925~precise
ros-fuerte-pr2-tuck-arms-app : 0.1.0-s1356575489~precise -> 0.1.0-s1360634647~precise
ros-fuerte-pr2-web-apps : 0.4.1-s1356581678~precise -> 0.4.1-s1360659064~precise
ros-fuerte-prosilica-driver : 1.8.0-s1347169057~precise -> 1.8.0-s1359905252~precise
ros-fuerte-protobuf : 0.1.0-s1347128313~precise -> 0.1.0-s1359883067~precise
ros-fuerte-python-qt-binding : 0.1.9-s1348595482~precise -> 0.1.9-s1359873126~precise
ros-fuerte-qt-gui-core : 0.1.4-s1355380879~precise -> 0.1.4-s1359888001~precise
ros-fuerte-qt-ros : 0.1.1-s1347128330~precise -> 0.1.1-s1359883100~precise
ros-fuerte-rail-cv-project : 0.1.0-s1356583715~precise -> 0.1.0-s1360639097~precise
ros-fuerte-rail-gazebo : 0.0.12-s1354692032~precise -> 0.0.12-s1360028380~precise
ros-fuerte-rail-maps : 0.0.1-s1352978091~precise -> 0.0.1-s1359838988~precise
ros-fuerte-random-numbers : 0.1.1-0precise-20120908-1623-+0000 -> 0.1.1-0precise-20130211-0932-+0000
ros-fuerte-reconfigure-gui : 0.1.0-s1355476224~precise -> 0.1.0-s1360629431~precise
ros-fuerte-remote-lab : 0.3.2-s1356583283~precise -> 0.3.2-s1360669314~precise
ros-fuerte-riq-hand : 0.1.3-s1356573877~precise -> 0.1.3-s1359910121~precise
ros-fuerte-rms : 0.1.1-s1352977046~precise -> 0.2.0-s1359839048~precise
ros-fuerte-rms-rovio-environment : 0.1.0-s1352980667~precise -> 0.1.0-s1360284278~precise
ros-fuerte-robot : 1.0.0-s1347207967~precise -> 1.0.0-s1360714896~precise
ros-fuerte-robot-contact-point : 0.1.0-s1347141399~precise -> 0.1.0-s1359894502~precise
ros-fuerte-robot-model : 1.8.1-s1347133837~precise -> 1.8.1-s1359887480~precise
ros-fuerte-robot-model-py : 0.2.0-s1347128366~precise -> 0.2.0-s1359883068~precise
ros-fuerte-robot-model-tutorials : 0.1.2-s1347122771~precise -> 0.1.2-s1359839096~precise
ros-fuerte-robot-model-visualization : 0.1.2-s1347128386~precise -> 0.1.2-s1359883118~precise
ros-fuerte-robot-pose-publisher : 0.1.01-s1351635823~precise -> 0.1.01-s1359887431~precise
ros-fuerte-romeo : 0.2.0-s1347122865~precise -> 0.2.0-s1359839073~precise
ros-fuerte-ros : 1.8.10-0precise-20120908-1636-+0000 -> 1.8.10-0precise-20130202-2019-+0000
ros-fuerte-ros-comm : 1.8.15-0precise-20120908-1740-+0000 -> 1.8.15-0precise-20130203-0847-+0000
ros-fuerte-ros-control : 0.0.2-s1356568846~precise -> 0.0.2-s1359894506~precise
ros-fuerte-ros-controllers : 0.0.1-s1356569380~precise -> 0.0.1-s1360583787~precise
ros-fuerte-ros-realtime : 0.5.3-s1347128289~precise -> 0.5.3-s1359883077~precise
ros-fuerte-ros-tutorials : 0.2.19-0precise-20120925-1930-+0000 -> 0.2.20-0precise-20130208-2359-+0000
ros-fuerte-rosbridge-suite : 0.2.1-s1352977275~precise -> 0.2.1-s1359887704~precise
ros-fuerte-rosconsole-bridge : 0.1.0-0precise-20120908-1813-+0000 -> 0.1.0-0precise-20130211-0937-+0000
ros-fuerte-roscpp-core : 0.2.6-0precise-20120908-1645-+0000 -> 0.2.6-0precise-20130202-2054-+0000
ros-fuerte-rosdoc-lite : 0.1.3-0precise-20121025-2242-+0000 -> 0.1.3-0precise-20130203-0631-+0000
ros-fuerte-rosh-core : 0.6.0-s1349115443~precise -> 0.6.0-s1359883144~precise
ros-fuerte-rosh-desktop-plugins : 0.4.0-s1355471924~precise -> 0.4.0-s1360629336~precise
ros-fuerte-rosh-robot-plugins : 0.4.1-s1347138060~precise -> 0.4.1-s1360621680~precise
ros-fuerte-roshpit : 0.4.1-s1355475373~precise -> 0.4.1-s1360634039~precise
ros-fuerte-rosjs : 0.0.15-s1348521532~precise -> 0.0.15-s1359839114~precise
ros-fuerte-roslisp-common : 0.2.1-s1347134075~precise -> 0.2.1-s1359888808~precise
ros-fuerte-roslisp-support : 0.3.1-s1347128339~precise -> 0.3.1-s1359883489~precise
ros-fuerte-rospack : 2.0.13-0precise-20130202-0924-+0000 -> 2.0.13-1precise-20120908-1622-+0000
ros-fuerte-rosserial : 0.2.0-s1347133840~precise -> 0.2.0-s1359887532~precise
ros-fuerte-rovio : 0.1.0-s1351661570~precise -> 0.1.0-s1359965109~precise
ros-fuerte-rqt : 0.1.6-s1355471980~precise -> 0.1.6-s1360620793~precise
ros-fuerte-rtt-common-msgs : 2.6.0-1-s1356248817~precise -> 2.6.0-1-s1359898873~precise
ros-fuerte-rtt-geometry : 0.3.0-s1356505368~precise -> 0.3.0-s1359907729~precise
ros-fuerte-rtt-ros-comm : 2.6.0-1-s1356247815~precise -> 2.6.0-1-s1359889574~precise
ros-fuerte-rtt-ros-integration : 2.6.0-1-s1356246942~precise -> 2.6.0-1-s1359883886~precise
ros-fuerte-rx : 1.8.9-0precise-20121114-0631-+0000 -> 1.8.9-0precise-20130204-2124-+0000
ros-fuerte-sbpl : 1.1.0-5precise-20120908-1815-+0000 -> 1.1.4-0precise-20130203-1041-+0000
ros-fuerte-serial-communication : 0.1.0-s1347128530~precise -> 0.1.0-s1359883225~precise
ros-fuerte-shadow-robot : 1.1.0-s1356579601~precise -> 1.1.0-s1360663371~precise
ros-fuerte-shadow-robot-ethercat : 1.1.0-s1356581534~precise -> 1.1.0-s1360676576~precise
ros-fuerte-shape-tools : 0.1.8-0precise-20120908-1811-+0000 -> 0.1.8-0precise-20130211-0944-+0000
ros-fuerte-simple-arms : 0.4.2-s1355476600~precise -> 0.4.2-s1360623563~precise
ros-fuerte-simulator-gazebo : 1.6.16-s1347172830~precise -> 1.6.16-s1360023516~precise
ros-fuerte-simulators : 1.0.0-s1347207967~precise -> 1.0.0-s1360714896~precise
ros-fuerte-slam-gmapping : 1.2.7-s1350948390~precise -> 1.2.7-s1360621552~precise
ros-fuerte-slam-karto : 0.4.0-s1347133867~precise -> 0.4.0-s1359887770~precise
ros-fuerte-sql-database : 0.3.0-s1347128344~precise -> 0.3.0-s1359884374~precise
ros-fuerte-sr-config : 1.1.1-s1354237486~precise -> 1.1.1-s1359839650~precise
ros-fuerte-sr-teleop : 1.1.0-s1356586716~precise -> 1.1.0-s1360667512~precise
ros-fuerte-sr-visualization : 1.1.0-s1356582564~precise -> 1.1.0-s1360692377~precise
ros-fuerte-srdfdom : 0.1.1-0precise-20121011-0155-+0000 -> 0.1.1-0precise-20130211-0944-+0000
ros-fuerte-srs-common : 0.1.0-s1355476738~precise -> 0.1.0-s1360623660~precise
ros-fuerte-stage : 1.6.6-s1347133988~precise -> 1.6.6-s1359887529~precise
ros-fuerte-std-msgs : 0.4.11-0precise-20120908-1717-+0000 -> 0.4.11-0precise-20130203-0840-+0000
ros-fuerte-swig-wx : 1.3.29-2precise-20130204-2121-+0000 -> 1.3.29-3precise-20120908-1623-+0000
ros-fuerte-symbolic-planning : 0.2.0-s1351204659~precise -> 0.2.0-s1360583856~precise
ros-fuerte-turtlebot : 1.0.2-s1356649086~precise -> 1.0.2-s1360400023~precise
ros-fuerte-turtlebot-apps : 1.0.1-s1351660964~precise -> 1.0.1-s1360634634~precise
ros-fuerte-turtlebot-simulator : 1.0.1-s1356649942~precise -> 1.0.1-s1360403896~precise
ros-fuerte-turtlebot-viz : 1.0.1-s1356649837~precise -> 1.0.1-s1360404024~precise
ros-fuerte-unique-identifier : 0.8.0-s1347128487~precise -> 0.8.0-s1359883359~precise
ros-fuerte-universal-robot : 0.2.3-s1348794528~precise -> 0.2.3-s1360620238~precise
ros-fuerte-urdfdom : 0.2.3-1precise-20121011-0155-+0000 -> 0.2.3-3precise-20130207-2029-+0000
ros-fuerte-urdfdom-headers : 0.2.1-1precise-20121011-0152-+0000 -> 0.2.1-4precise-20130207-2026-+0000
ros-fuerte-utexas-art : 1.0.0-s1355574845~precise -> 1.0.0-s1360714896~precise
ros-fuerte-velodyne : 0.9.1-s1347171439~precise -> 0.9.1-s1360023242~precise
ros-fuerte-velodyne-utils : 0.3.0-s1347172411~precise -> 0.3.0-s1360025428~precise
ros-fuerte-vision-opencv : 1.8.8-s1349900876~precise -> 1.8.8-s1360280127~precise
ros-fuerte-vision-visp : 0.5.0-s1349907504~precise -> 0.5.0-s1360283601~precise
ros-fuerte-visualization : 1.8.17-s1355467586~precise -> 1.8.17-s1360025917~precise
ros-fuerte-visualization-common : 1.8.4-s1347128602~precise -> 1.8.4-s1359883358~precise
ros-fuerte-visualization-tutorials : 0.6.3-s1355472237~precise -> 0.6.3-s1360029651~precise
ros-fuerte-viz : 1.0.0-s1355574845~precise -> 1.0.0-s1360714896~precise
ros-fuerte-warehousewg : 0.6.5-s1348595052~precise -> 0.6.5-s1359887518~precise
ros-fuerte-web-interface : 0.5.0-s1349902798~precise -> 0.5.0-s1360280610~precise
ros-fuerte-wg-common : 0.1.3-s1347122925~precise -> 0.1.3-s1359839167~precise
ros-fuerte-wg-pr2 : 1.0.0-s1356669545~precise -> 1.0.0-s1360714896~precise
ros-fuerte-wg-pr2-apps : 0.1.2-s1356580403~precise -> 0.1.2-s1360644999~precise
ros-fuerte-wge100-driver : 1.7.3-s1347169507~precise -> 1.7.3-s1359905224~precise
ros-fuerte-wifi-drivers : 0.1.5-s1347146093~precise -> 0.1.5-s1359906355~precise
ros-fuerte-xacro : 1.6.1-s1347128571~precise -> 1.6.1-s1359883505~precise
ros-fuerte-yujin-ocs : 0.1.1-s1356245241~precise -> 0.1.1-s1359909064~precise
ros-fuerte-zeroconf-avahi-suite : 0.1.9-s1354238002~precise -> 0.1.9-s1359888455~precise
ros-fuerte-zeroconf-msgs : 0.1.9-s1354228115~precise -> 0.1.9-s1359883569~precise
ros-groovy-arbotix : 0.6.1-s1359447800~precise -> 0.6.1-s1360643584~precise
ros-groovy-arm-navigation : 1.2.4-s1360100682~precise -> 1.2.4-s1360643165~precise
ros-groovy-arm-navigation-experimental : 0.5.11-s1360108520~precise -> 0.5.11-s1360663656~precise
ros-groovy-bosch-common : 0.1.5-s1360308699~precise -> 0.1.5-s1360591549~precise
ros-groovy-brown-remotelab : 0.0.9-s1359969329~precise -> 0.0.9-s1360660816~precise
ros-groovy-calibration : 0.9.24-0precise-20130205-2155-+0000 -> 0.9.24-0precise-20130211-2341-+0000
ros-groovy-camera-calibration : 1.10.4-0precise-20130202-1409-+0000 -> 1.10.4-0precise-20130211-1040-+0000
ros-groovy-care-o-bot : 1.0.0-s1360330219~precise -> 1.0.0-s1360719758~precise
ros-groovy-care-o-bot-desktop : 1.0.0-s1360330219~precise -> 1.0.0-s1360719758~precise
ros-groovy-care-o-bot-robot : 1.0.0-s1360313729~precise -> 1.0.0-s1360719758~precise
ros-groovy-compressed-depth-image-transport : 1.8.18-0precise-20130208-0322-+0000 -> 1.8.18-0precise-20130211-0957-+0000
ros-groovy-compressed-image-transport : 1.8.18-0precise-20130208-0320-+0000 -> 1.8.18-0precise-20130211-0954-+0000
ros-groovy-continuous-ops : 0.4.3-s1360135548~precise -> 0.4.3-s1360680746~precise
ros-groovy-control : 1.1.5-0precise-20130125-0508-+0000 -> 1.1.6-0precise-20130212-0256-+0000
ros-groovy-control-msgs : 1.1.5-0precise-20130125-0446-+0000 -> 1.1.6-0precise-20130212-0200-+0000
ros-groovy-cv-bridge : 1.10.4-0precise-20130202-1344-+0000 -> 1.10.5-0precise-20130211-0811-+0000
ros-groovy-depth-image-proc : 1.10.4-0precise-20130205-2058-+0000 -> 1.10.4-0precise-20130211-1034-+0000
ros-groovy-depthimage-to-laserscan : 1.0.4-0precise-20130202-1414-+0000 -> 1.0.4-0precise-20130211-1041-+0000
ros-groovy-desktop : 1.0.0-s1360330218~precise -> 1.0.0-s1360719758~precise
ros-groovy-desktop-full : 1.0.0-s1360330219~precise -> 1.0.0-s1360719758~precise
ros-groovy-dynamixel-motor : 0.2.3-s1359158282~precise -> 0.2.3-s1360643451~precise
ros-groovy-dynamixel-motor-experimental : 0.1.0-s1359450416~precise -> 0.1.0-s1360643219~precise
ros-groovy-erratic-robot : 0.3.2-s1360130694~precise -> 0.3.2-s1360664986~precise
ros-groovy-graspit-simulator : 0.4.1-s1360308824~precise -> 0.4.1-s1360685403~precise
ros-groovy-hector-slam : 0.2.2-s1360222581~precise -> 0.2.2-s1360591783~precise
ros-groovy-hector-worldmodel : 0.2.0-s1360224194~precise -> 0.2.0-s1360626935~precise
ros-groovy-ias-common : 0.1.3-s1360105347~precise -> 0.1.3-s1360660550~precise
ros-groovy-image-cb-detector : 0.9.24-0precise-20130205-2058-+0000 -> 0.9.24-0precise-20130211-1003-+0000
ros-groovy-image-geometry : 1.10.4-0precise-20130202-1346-+0000 -> 1.10.5-0precise-20130211-0820-+0000
ros-groovy-image-pipeline : 1.10.4-0precise-20130205-2106-+0000 -> 1.10.4-0precise-20130211-2351-+0000
ros-groovy-image-proc : 1.10.4-0precise-20130202-1412-+0000 -> 1.10.4-0precise-20130211-1037-+0000
ros-groovy-image-rotate : 1.10.4-0precise-20130202-1353-+0000 -> 1.10.4-0precise-20130211-1003-+0000
ros-groovy-image-transport-plugins : 1.8.18-0precise-20130208-0327-+0000 -> 1.8.18-0precise-20130211-1321-+0000
ros-groovy-image-view : 1.10.4-0precise-20130202-1352-+0000 -> 1.10.4-0precise-20130211-0959-+0000
ros-groovy-kingfisher : 0.1.1-s1360294415~precise -> 0.1.1-s1360632560~precise
ros-groovy-kingfisher-desktop : 1.0.0-s1360313729~precise -> 1.0.0-s1360719758~precise
ros-groovy-kingfisher-robot : 1.0.0-s1360313729~precise -> 1.0.0-s1360719758~precise
ros-groovy-kobuki : 0.2.4-s1360100284~precise -> 0.3.4-0precise-20130211-1100-+0000
ros-groovy-kobuki-msgs : 0.2.0-s1359158336~precise -> 0.3.1-0precise-20130209-0710-+0000
ros-groovy-laser-cb-detector : 0.9.24-0precise-20130205-2109-+0000 -> 0.9.24-0precise-20130211-1323-+0000
ros-groovy-mjpeg-server : 1.0.2-s1359819220~precise -> 1.0.2-s1360591664~precise
ros-groovy-move-arm : 1.0.0-s1360222160~precise -> 1.0.0-s1360719758~precise
ros-groovy-moveit-full : 0.3.1-0precise-20130206-2357-+0000 -> 0.3.1-0precise-20130212-0231-+0000
ros-groovy-moveit-full-pr2 : 0.3.1-0precise-20130207-0015-+0000 -> 0.3.1-0precise-20130212-0913-+0000
ros-groovy-moveit-pr2 : 0.3.7-0precise-20130206-1807-+0000 -> 0.3.7-0precise-20130212-0440-+0000
ros-groovy-moveit-ros : 0.3.21-0precise-20130206-2315-+0000 -> 0.3.21-0precise-20130212-0148-+0000
ros-groovy-moveit-ros-benchmarks : 0.3.21-0precise-20130206-2158-+0000 -> 0.3.21-0precise-20130212-0006-+0000
ros-groovy-moveit-ros-visualization : 0.3.21-0precise-20130206-2035-+0000 -> 0.3.21-0precise-20130211-2009-+0000
ros-groovy-moveit-setup-assistant : 0.3.4-0precise-20130206-2157-+0000 -> 0.3.4-0precise-20130212-0004-+0000
ros-groovy-moveit-source-build-deps : 0.3.1-0precise-20130205-2057-+0000 -> 0.3.1-0precise-20130212-0254-+0000
ros-groovy-nasa-r2-common : 0.0.2-s1360095517~precise -> 0.0.2-s1360627489~precise
ros-groovy-nasa-r2-simulator : 0.0.3-s1360130833~precise -> 0.0.3-s1360665230~precise
ros-groovy-object-manipulation : 0.7.1-s1360117823~precise -> 0.7.1-s1360668664~precise
ros-groovy-object-recognition-ros : 0.1.13-0precise-20130207-0151-+0000 -> 0.1.13-0precise-20130211-2006-+0000
ros-groovy-octomap-mapping : 0.4.8-s1360105052~precise -> 0.4.8-s1360660627~precise
ros-groovy-openni-launch : 1.8.3-0precise-20130205-2111-+0000 -> 1.8.3-0precise-20130211-1415-+0000
ros-groovy-people : 0.1.4-s1360309205~precise -> 0.1.4-s1360632453~precise
ros-groovy-perception : 1.0.0-s1360313729~precise -> 1.0.0-s1360719758~precise
ros-groovy-pr2 : 1.0.0-s1360313729~precise -> 1.0.0-s1360719758~precise
ros-groovy-pr2-applications : 1.0.0-s1360313729~precise -> 1.0.0-s1360719758~precise
ros-groovy-pr2-apps : 0.5.0-s1360120455~precise -> 0.5.0-s1360667715~precise
ros-groovy-pr2-arm-navigation : 0.5.2-s1360126885~precise -> 0.5.2-s1360668570~precise
ros-groovy-pr2-base : 1.0.0-s1360313729~precise -> 1.0.0-s1360719758~precise
ros-groovy-pr2-calibration : 1.4.0-s1360128782~precise -> 1.4.0-s1360678982~precise
ros-groovy-pr2-common-actions : 0.4.0-s1360111023~precise -> 0.4.0-s1360663638~precise
ros-groovy-pr2-controllers : 1.9.0-s1359967319~precise -> 1.9.0-s1360643492~precise
ros-groovy-pr2-desktop : 1.0.0-s1360330219~precise -> 1.0.0-s1360719758~precise
ros-groovy-pr2-interactive-manipulation : 1.0.0-s1360330219~precise -> 1.0.0-s1360719758~precise
ros-groovy-pr2-kinematics : 0.5.0-s1360104884~precise -> 0.5.0-s1360660649~precise
ros-groovy-pr2-mannequin-mode-app : 0.1.0-s1360129222~precise -> 0.1.0-s1360678443~precise
ros-groovy-pr2-moveit-plugins : 0.3.7-0precise-20130206-0944-+0000 -> 0.3.7-0precise-20130212-0256-+0000
ros-groovy-pr2-navigation : 0.1.14-s1360129596~precise -> 0.1.14-s1360677469~precise
ros-groovy-pr2-navigation-apps : 0.1.1-s1360135469~precise -> 0.1.1-s1360692026~precise
ros-groovy-pr2-object-manipulation : 0.7.1-s1360133655~precise -> 0.7.1-s1360684703~precise
ros-groovy-pr2-pan-tilt : 0.1.0-s1359970938~precise -> 0.1.0-s1360661024~precise
ros-groovy-pr2-plugs : 0.6.4-s1360121805~precise -> 0.6.4-s1360667678~precise
ros-groovy-pr2-props-app : 0.1.0-s1360146997~precise -> 0.1.0-s1360700873~precise
ros-groovy-pr2-props-stack : 0.1.0-s1360140842~precise -> 0.1.0-s1360697146~precise
ros-groovy-pr2-ps3-joystick-app : 0.1.0-s1360129157~precise -> 0.1.0-s1360679094~precise
ros-groovy-pr2-robot : 1.5.0-s1360121895~precise -> 1.5.0-s1360662960~precise
ros-groovy-pr2-self-test : 0.4.0-s1360133086~precise -> 0.4.0-s1360677754~precise
ros-groovy-pr2-simulator : 1.9.2-s1360121715~precise -> 1.9.2-s1360660977~precise
ros-groovy-pr2-teleop-app : 0.1.0-s1360129747~precise -> 0.1.0-s1360678333~precise
ros-groovy-pr2-tuck-arms-app : 0.1.0-s1360120419~precise -> 0.1.0-s1360668482~precise
ros-groovy-pr2-web-apps : 0.4.1-s1360145835~precise -> 0.4.1-s1360696597~precise
ros-groovy-ros-full : 1.0.0-s1359872576~precise -> 1.0.0-s1360719758~precise
ros-groovy-rosh-desktop-plugins : 0.4.0-s1360095439~precise -> 0.4.0-s1360627642~precise
ros-groovy-roshpit : 0.4.1-s1360096581~precise -> 0.4.1-s1360633707~precise
ros-groovy-rqt-common-plugins : 0.2.10-0precise-20130202-1459-+0000 -> 0.2.10-0precise-20130211-1320-+0000
ros-groovy-rqt-image-view : 0.2.10-0precise-20130202-1359-+0000 -> 0.2.10-0precise-20130211-0957-+0000
ros-groovy-rqt-pr2-dashboard : 0.2.3-s1360093187~precise -> 0.2.3-s1360633365~precise
ros-groovy-rqt-robot-plugins : 0.2.8-0precise-20130205-1931-+0000 -> 0.2.8-0precise-20130212-0002-+0000
ros-groovy-rqt-rviz : 0.2.8-0precise-20130205-1928-+0000 -> 0.2.8-0precise-20130211-2009-+0000
ros-groovy-rviz : 1.9.20-0precise-20130205-1908-+0000 -> 1.9.20-0precise-20130211-1044-+0000
ros-groovy-rviz-animated-view-controller : 0.1.0-s1360093012~precise -> 0.1.0-s1360612753~precise
ros-groovy-simple-arms : 0.4.2-s1360105104~precise -> 0.4.2-s1360660839~precise
ros-groovy-simulators : 1.0.0-s1360222160~precise -> 1.0.0-s1360719758~precise
ros-groovy-sr-ronex : 0.9.0-s1360222833~precise -> 0.9.0-s1360668494~precise
ros-groovy-stereo-image-proc : 1.10.4-0precise-20130202-1538-+0000 -> 1.10.4-0precise-20130211-1412-+0000
ros-groovy-theora-image-transport : 1.8.18-0precise-20130208-0320-+0000 -> 1.8.18-0precise-20130211-0959-+0000
ros-groovy-turtlebot-create : 1.9.1-s1359160629~precise -> 2.0.0-s1360482458~precise
ros-groovy-turtlebot-create-desktop : 1.9.0-s1360093315~precise -> 2.0.0-s1360634017~precise
ros-groovy-turtlebot-simulator : 1.9.1-s1360106609~precise -> 1.9.1-s1360495011~precise
ros-groovy-universal-robot : 0.2.2-s1359534185~precise -> 0.2.2-s1360643673~precise
ros-groovy-utexas-art : 1.0.0-s1360313729~precise -> 1.0.0-s1360719758~precise
ros-groovy-velo-gripper : 0.1.0-s1359969401~precise -> 0.1.0-s1360661018~precise
ros-groovy-vision-opencv : 1.10.4-0precise-20130202-1411-+0000 -> 1.10.5-0precise-20130211-1036-+0000
ros-groovy-vision-visp : 0.5.0-s1360102031~precise -> 0.5.0-s1360632516~precise
ros-groovy-visualization : 1.9.2-s1360094395~precise -> 1.9.2-s1360613199~precise
ros-groovy-visualization-tutorials : 0.7.4-s1360309036~precise -> 0.7.4-s1360612869~precise
ros-groovy-viz : 1.0.0-s1360222160~precise -> 1.0.0-s1360719758~precise
ros-groovy-web-interface : 0.5.0-s1359819622~precise -> 0.5.0-s1360591792~precise
ros-groovy-wg-pr2 : 1.0.0-s1360313729~precise -> 1.0.0-s1360719758~precise
ros-groovy-wg-pr2-apps : 0.1.2-s1360137879~precise -> 0.1.2-s1360692452~precise
ros-groovy-yujin-ocs : 0.1.3-s1359456071~precise -> 0.2.2-0precise-20130209-1840-+0000
