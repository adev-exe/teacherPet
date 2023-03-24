import imp
from flask import (
    Blueprint, render_template, url_for, request
)
import util

views = Blueprint('views', __name__)

# credidatials
username = 'me'
password = 'test'
host = '127.0.0.1'
port = '5432'
database = 'KybPartPickerInventory'


@views.route('/')
@views.route('/base.html')
def home():
    return render_template("base.html", title="Keyboard Part Picker")

@views.route('/bulidGuide.html')
def bulid_guide():
    pcb = '''
        The PCB is the most important part of the keyboard. It is what gives the keyboard life. When trying to come up with a build,
        there are centain sizes of PCB that we recommend to stick to, 60 % , 75%, 80 % , 90%, and 100%. 
        The reason for this is that these sizes have the most support and components on the market right now. In addition 
        to thinking about the size of the PCB, you must think about the type of PCB you want for your build. 
        For the beginner level, we suggest a Hot-Swappable PCB as there 
        is no soldering at all. If you fancy yourself handy with electronics then you can either go for a 
        Standard PCB or a Through-hole PCB. The Standard only requires you to solder the switches and the 
        Through-hole requires you to solder everything from diodes to the USB connector.
        '''

    case = '''
        The Case is what holds all of the components and is one of the main factors that contributes the the
        sound generated from a keyboard. Cases come in many type of material such as plastic, wood, carbon
        fiber, aluminium, etc. As such whatever case you do choose will be impacted by whatever size of PCB you decide 
        on so be wary when making this decision.
        '''

    plate = '''
        MAJOR NOTE: If you get 5-pin switches, a plate may not be necessary as these can be used for purely PCB mounted switch builds.
        The Plate is a key component in how it will act together with the PCB and the Switches. It is a guard between the two so that if 
        you were heavy-handed, your key presses would not affect the structure of the PCB. Plates are made in accompaniment with PCB's so
        specific plates will only align with specific PCB's. Therefore, much like the case, the plate is also reliant on what choice of PCB
        you have made. As for what plates are made of, they are generally going to be composed of aluminum, brass, polycarbonate, and carbon fiber.
    '''

    stabilizers = '''             
      Stabilizers are an auxillary part when it comes to a keyboard, but it is still vital to the functionality of the entire board.
      They are a part that is essential when trying to have your keyboard sound good as well as keeping larger keys like SHIFT, ENTER, 
      CTRL, and Spacebar stable.
      '''

    switches = '''
    The Switches are what interact with the PCB to make your key presses happen. Switches are made of a housing which can have 5 or 3 pins,
    a spring that varies in weight to give the switch a particular feel, and the stem which works with the spring and housing to determine 
    what feel and sound the switch will produce. With switches there are three profiles that you can choose from, these are based on the sound 
    and feeling that they create. There is Linear which is where the switch is quieter and the press is smooth with little to no feedback, Tactile 
    which gives you a bit of press feedback and some sound, and Clicky which focuses on giving you press feedback and a particularly "clicky" sound.
    '''

    keycaps = ''' 
        The Keycaps are the primary aesthetic builder when it comes to keyboard building. They are what makes you keyboard look good and are generally
        what theme or personality your build has. When finding keycaps, it is important that you know which kind of layout your PCB is set in. There are 
        two layouts that you as a builder/hobbyist will need to keep in mind, ANSI and ISO. The main difference between the two is the Enter key, but there 
        other minor differences as well. For an ANSI board the Enter key is a normal rectangle whereas for an ISO board the Enter is an upside-down "L". 
        In addition to layout, keycaps are offered in different material and profiles. The materials they are made of determine their feel and look and the
        profile they have determine the flatness or concavity of the keycap. 
    '''

    images = ['img/pcb.jpeg', 'img/case.jpeg', 'img/plate.jpeg',
              'img/stabs.jpeg', 'img/switches.jpeg', 'img/kcps.jpeg']
    paragraph = [pcb, case, plate, stabilizers, switches, keycaps]
    return render_template("bulidGuide.html", title="Build Guide", paragraph=paragraph, images=images)



@views.route('/bulidPage.html')
def bulid_page():
    return render_template("bulidPage.html", title="Build Page",)


@views.route('/teamMem.html')
def team_member():
    return render_template("teamMem.html", title="Team Member Page",)

@views.route('/tutor.html')
def tutor():
    return render_template("tutor.html", title="Tutor",)

@views.route('partsSelection/pcb.html')
def pcb():
    cursor, connection = util.connect_to_db(
        username, password, host, port, database)
    # execute SQL commands
    record = util.fetch_case(
        cursor, sql_string="select pcb_name, pcb_url, pcb_price from product_pcb;")
    if record == -1:
        print('Something is wrong with the SQL command')
    else:
        # this will return all column names of the select result table
        # col_names = [desc[0] for desc in cursor.description]
        # only use the first five rows
        # log = record[10]
        #  print("test”)I
        log = []
        for i in record:
            log.append(i)

        # log=[[1,2],[3,4]]
    # disconnect from database
    # print('Works')
    util.disconnect_from_db(connection, cursor)
    
    return render_template("partsSelection/pcb.html", title="PCB Page", pcb_name=log)


@views.route('partsSelection/case.html', methods=('GET', 'POST'))
def case():
    cursor, connection = util.connect_to_db(
        username, password, host, port, database)
    # execute SQL commands
    record = util.fetch_case(
        cursor, sql_string="select case_name, case_url, case_price from product_case;")
    if record == -1:
        print('Something is wrong with the SQL command')
    else:
        # this will return all column names of the select result table
        # col_names = [desc[0] for desc in cursor.description]
        # only use the first five rows
        # log = record[10]
        #  print("test”)I
        log = []
        index = 0
        for i in record:
            log.append(i)
            # index +=1

    if request.method == 'POST':
        index = request.form['index']
        print("request")
        # log=[[1,2],[3,4]]
    # disconnect from database
    # print('Works')
    util.disconnect_from_db(connection, cursor)
    return render_template("partsSelection/case.html", title="Case Page", case_name=log, index =index)


@views.route('partsSelection/plate.html')
def plate():
    cursor, connection = util.connect_to_db(
        username, password, host, port, database)
    # execute SQL commands
    record = util.fetch_case(
        cursor, sql_string="select plate_name, plate_url , plate_price from product_plate;")
    if record == -1:
        print('Something is wrong with the SQL command')
    else:
        # this will return all column names of the select result table
        # col_names = [desc[0] for desc in cursor.description]
        # only use the first five rows
        # log = record[10]
        #  print("test”)I
        log = []
        for i in record:
            log.append(i)

        # log=[[1,2],[3,4]]
    # disconnect from database
    # print('Works')
    util.disconnect_from_db(connection, cursor)
    return render_template("partsSelection/plate.html", title="Plate Page", plate_name=log)


@views.route('partsSelection/stabilizers.html')
def stabilizers():
    cursor, connection = util.connect_to_db(
        username, password, host, port, database)
    # execute SQL commands
    record = util.fetch_case(
        cursor, sql_string="select stabilizer_name, stabilizer_url ,stabilizer_price from product_stabilizers;")
    if record == -1:
        print('Something is wrong with the SQL command')
    else:
        # this will return all column names of the select result table
        # col_names = [desc[0] for desc in cursor.description]
        # only use the first five rows
        # log = record[10]
        #  print("test”)I
        log = []
        for i in record:
            log.append(i)

        # log=[[1,2],[3,4]]
    # disconnect from database
    # print('Works')
    util.disconnect_from_db(connection, cursor)
    return render_template("partsSelection/stabilizers.html", title="Stabilizers Page",stabilizer_name=log)


@views.route('partsSelection/switches.html')
def switches():
    cursor, connection = util.connect_to_db(
        username, password, host, port, database)
    # execute SQL commands
    record = util.fetch_case(
        cursor, sql_string="select switches_name, switches_url , switches_price from product_switches;")
    if record == -1:
        print('Something is wrong with the SQL command')
    else:
        # this will return all column names of the select result table
        # col_names = [desc[0] for desc in cursor.description]
        # only use the first five rows
        # log = record[10]
        #  print("test”)I
        log = []
        for i in record:
            log.append(i)

        # log=[[1,2],[3,4]]
    # disconnect from database
    # print('Works')
    util.disconnect_from_db(connection, cursor)
    return render_template("partsSelection/switches.html", title="Switches Page",switch_name=log)


@views.route('partsSelection/keycaps.html')
def keycaps():
    cursor, connection = util.connect_to_db(
        username, password, host, port, database)
    # execute SQL commands
    record = util.fetch_case(
        cursor, sql_string="select keycaps_name, keycaps_url , keycaps_price from product_keycaps;")
    if record == -1:
        print('Something is wrong with the SQL command')
    else:
        # this will return all column names of the select result table
        # col_names = [desc[0] for desc in cursor.description]
        # only use the first five rows
        # log = record[10]
        #  print("test”)I
        log = []
        for i in record:
            log.append(i)

        # log=[[1,2],[3,4]]
    # disconnect from database
    # print('Works')
    util.disconnect_from_db(connection, cursor)
    return render_template("partsSelection/keycaps.html", title="Keycaps Page",keycap_name=log)

@views.route('currentBulid.html')
def current_bulid():
     return render_template("currentBulid.html", title="Current Build Page")
