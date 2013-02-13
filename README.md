buildfarm_sync_report
=====================

To use this script execute the following:

python syncdiff.py *beforefile* *afterfile*

What follows is an example output for syncdiff run on the following files: (if viewing in github view in raw for real results)

http://packages.ros.org/ros/ubuntu/dists/precise/main/binary-amd64/Packages

http://packages.ros.org/ros-shadow-fixed/ubuntu/dists/precise/main/binary-amd64/Packages


Packages Added: 
ros-fuerte-applanix-driver : 0.1.0
ros-fuerte-extremum-seeking : 0.1.0
ros-fuerte-humanoid-navigation : 0.4.0
ros-fuerte-husky-apps : 0.1.0
ros-fuerte-husky-desktop : 1.0.0
ros-fuerte-husky-robot : 1.0.0
ros-fuerte-husky-simulator : 0.1.0
ros-fuerte-object-recognition-renderer : 0.1.8
ros-fuerte-object-recognition-tabletop : 0.2.17
ros-fuerte-rms-pr2-gazebo-environment : 0.1.0
ros-fuerte-saliency-detection : 0.1.2
ros-fuerte-shared-serial : 0.1.0
ros-fuerte-speakeasy : 0.1.1
ros-fuerte-sr-ronex : 0.9.0.2
ros-fuerte-velo-gripper : 0.1.0
ros-fuerte-webmap : 0.1.0
ros-groovy-cmd-vel-mux : 0.2.2
ros-groovy-kobuki-arm : 0.3.4
ros-groovy-kobuki-auto-docking : 0.3.4
ros-groovy-kobuki-bumper2pc : 0.3.4
ros-groovy-kobuki-controller-tutorial : 0.3.4
ros-groovy-kobuki-driver : 0.3.4
ros-groovy-kobuki-ftdi : 0.3.4
ros-groovy-kobuki-keyop : 0.3.4
ros-groovy-kobuki-node : 0.3.4
ros-groovy-kobuki-safety-controller : 0.3.4
ros-groovy-kobuki-testsuite : 0.3.4
ros-groovy-yocs-controllers : 0.2.2
ros-groovy-yocs-velocity-smoother : 0.2.2

Packages Removed: 
ros-fuerte-care-o-bot : 1.0.0
ros-fuerte-care-o-bot-desktop : 1.0.0
ros-fuerte-care-o-bot-robot : 1.0.0
ros-fuerte-clearpath-husky-robot : 1.0.0
ros-fuerte-cob-robots : 0.4.6
ros-fuerte-cob-simulation : 0.4.5
ros-fuerte-moveit-core : 0.1.4
ros-fuerte-openrtm : 1.1.0
ros-fuerte-rocon-comms : 0.1.1
ros-fuerte-rocon-msgs : 0.1.4
ros-fuerte-rocon-multimaster : 0.1.9
ros-fuerte-schunk-modular-robotics : 0.4.4
ros-fuerte-schunk-robots : 0.1.2
ros-fuerte-schunk-simulation : 0.1.2
ros-fuerte-zeroconf-comms : 0.1.6
ros-fuerte-zeroconf-implementations : 0.1.6
ros-groovy-kobuki-desktop : 0.1.3
ros-groovy-turtlebot : 1.9.4
ros-groovy-turtlebot-apps : 1.9.2
ros-groovy-turtlebot-dashboard : 0.1.0
ros-groovy-turtlebot-viz : 1.9.3

Packages Updated: 
ros-fuerte-clearpath-husky : 0.3.1 -> 0.3.2
ros-fuerte-cob-calibration-data : 0.1.1 -> 0.1.2
ros-fuerte-cob-command-tools : 0.4.4 -> 0.4.6
ros-fuerte-cob-common : 0.4.5 -> 0.4.6
ros-fuerte-cob-driver : 0.4.8 -> 0.4.10
ros-fuerte-cob-environments : 0.4.3 -> 0.4.4
ros-fuerte-cob-extern : 0.4.2 -> 0.4.3
ros-fuerte-ecto : 0.4.16 -> 0.5.3
ros-fuerte-ecto-image-pipeline : 0.4.7 -> 0.4.8
ros-fuerte-ecto-opencv : 0.4.17 -> 0.4.21
ros-fuerte-ecto-openni : 0.3.7 -> 0.3.8
ros-fuerte-ecto-ros : 0.3.21 -> 0.3.23
ros-fuerte-ethzasl-icp-mapping : 0.9.0 -> 0.9.5
ros-fuerte-ethzasl-message-transport : 0.8.2 -> 0.8.3
ros-fuerte-flirtlib : 0.1.4 -> 0.1.5
ros-fuerte-freenect-stack : 0.1.0 -> 0.1.1
ros-fuerte-hector-gazebo : 0.1.1 -> 0.1.2
ros-fuerte-hector-models : 0.1.0 -> 0.1.1
ros-fuerte-hector-slam : 0.1.1 -> 0.2.2
ros-fuerte-humanoid-msgs : 0.1.1.1 -> 0.1.2
ros-fuerte-image-transport-plugins : 1.8.5 -> 1.8.6
ros-fuerte-joystick-drivers : 1.8.1 -> 1.8.2
ros-fuerte-kingfisher : 0.1.1 -> 0.1.2
ros-fuerte-librms : 0.0.1 -> 0.2.0
ros-fuerte-moveit-msgs : 0.2.7 -> 0.2.8
ros-fuerte-object-manipulation : 0.6.8 -> 0.6.9
ros-fuerte-object-recognition-capture : 0.2.15 -> 0.2.18
ros-fuerte-object-recognition-core : 0.4.11 -> 0.4.18
ros-fuerte-object-recognition-linemod : 0.2.5 -> 0.2.9
ros-fuerte-object-recognition-msgs : 0.3.11 -> 0.3.13
ros-fuerte-object-recognition-reconstruction : 0.2.15 -> 0.2.20
ros-fuerte-object-recognition-ros : 0.1.5 -> 0.1.13
ros-fuerte-object-recognition-tod : 0.4.9 -> 0.4.12
ros-fuerte-object-recognition-transparent-objects : 0.3.8 -> 0.3.12
ros-fuerte-octomap-mapping : 0.4.5 -> 0.4.6
ros-fuerte-opencv-candidate : 0.1.3 -> 0.1.8
ros-fuerte-orocos-toolchain : 2.6.0-3 -> 2.6.0.5
ros-fuerte-pr2-apps : 0.4.6 -> 0.5.0
ros-fuerte-pr2-object-manipulation : 0.6.6 -> 0.6.7
ros-fuerte-rms : 0.1.1 -> 0.2.0
ros-fuerte-ros-tutorials : 0.2.19 -> 0.2.20
ros-fuerte-sbpl : 1.1.0 -> 1.1.4
ros-groovy-control : 1.1.5 -> 1.1.6
ros-groovy-control-msgs : 1.1.5 -> 1.1.6
ros-groovy-cv-bridge : 1.10.4 -> 1.10.5
ros-groovy-image-geometry : 1.10.4 -> 1.10.5
ros-groovy-kobuki : 0.2.4 -> 0.3.4
ros-groovy-kobuki-msgs : 0.2.0 -> 0.3.1
ros-groovy-turtlebot-create : 1.9.1 -> 2.0.0
ros-groovy-turtlebot-create-desktop : 1.9.0 -> 2.0.0
ros-groovy-vision-opencv : 1.10.4 -> 1.10.5
ros-groovy-yujin-ocs : 0.1.3 -> 0.2.2
