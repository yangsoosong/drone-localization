def handleFileReceived(event, sender, data):
    # Create a file to receive image data from the drone.
    path = './tello-test.jpeg'
    with open(path, 'wb') as fd:
        fd.write(data)
    print('Saved photo to %s' % path)
