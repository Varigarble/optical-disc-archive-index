import pickle


class Disc:

    __copies=1

    def __init__(self, name="default", disc_type="not set", sub_type="",
                 burn_date=None, burn_verification=None, condition=None, creator=None,
                 data_compression=None, dupe_status=None, encryption=None,
                 disc_format=None, image_format=None, label=None, location="unknown",
                 multi_volume_id=None, password=None, project=None, supersession=None,
                 tag=None, txt_index_loc=None, txt_index_name=None, write_status=None):

        self.burn_date = burn_date
        self.burn_verification = burn_verification
        self.condition = condition
        # self.copies = copies
        self.creator = creator
        self.data_compression = data_compression
        self.dupe_status = dupe_status
        self.encryption = encryption
        self.disc_format = disc_format
        self.image_format = image_format
        self.label = label
        self.name = name  # Sharpie
        self.location = location
        self.multi_volume_id = multi_volume_id
        self.password = password
        self.project = project
        self.sub_type = sub_type
        self.supersession = supersession
        self.tag = tag
        self.txt_index_loc = txt_index_loc
        self.txt_index_name = txt_index_name
        self.disc_type = disc_type
        self.write_status = write_status

    def set_copies(self, copies):
        try:    
            if type(copies) == int and copies > 0:
                self.__copies = copies
            if type(copies) != int or copies <= 0:
                raise ValueError("PosInt")
        except ValueError:    
            print(f"Error in {self.name}: copies must be a positive integer", "\n")
            self.__copies = "ERR"

    def get_name(self):
        return self.name

    def __repr__(self):
        # addl1 and addl2 values will be updated if they differ from a default_disc object
        addl1 = ","
        addl2 = ""
        default_warning = ""
        change_count = 0

        if self.name == "default":
            default_warning = "DISC NAME HAS NOT BEEN SET!, " 
        if self.disc_type == "not set":
            self.sub_type = ""
        if self.disc_format != None:
            addl1 += " disc format: " + self.disc_format + ","
        
        addl1 = addl1[:-1]

        for key in self.__dict__:
            if key in default_disc.__dict__ and self.__dict__[key] != default_disc.__dict__[key]:
                addl2 += " " + key + ": " + str(self.__dict__[key]) + ","
                change_count += 1

        addl2 = addl2[:-1]

        return f"disc name: {self.name}, {default_warning}disc type: {self.disc_type}{self.sub_type}, copies: \
{self.__copies}, location: {self.location}" + addl1 + ". " + "\n" + "Changed fr. default: " + str(change_count) + ":" \
+ addl2


default_disc = Disc()  # Create a default_disc for subsequent discs to compare addl1 and addl2 values in __repr__ method

disc_1 = Disc(name="Lipslip's Lisp pseudo-corpse", location="unknown", dupe_status="backup", sub_type="-r",
              disc_format="video")

disc_1.set_copies(-3)

disc_2 = Disc(location="Hidden Valley Ranch", dupe_status="original", disc_type="vcd", sub_type="-r",
              burn_date="Nov. 2011 - May 2012")

disc_2.set_copies(2)

print("All discs: default_disc name: ", default_disc.get_name(), ". ", "disc_1 name: ", disc_1.get_name(), ". ",
      "disc_2 name: ", disc_2.get_name(), ".", "\n", sep='')

print("default_disc repr: ", repr(default_disc), sep="")
print("default_disc dict: ", default_disc.__dict__, "\n", sep="")

print("disc_1 repr: ", repr(disc_1), sep="")
print("disc_1 dict: ", disc_1.__dict__, "\n", sep="")

print("disc_2 repr: ", repr(disc_2), sep="")
print("disc_2 dict: ", disc_2.__dict__, "\n", sep="")

collection = ["***DISC***", default_disc, "***DISC***", disc_1, "***DISC***", disc_2]


def pickle_discs(spindle):
    with open("discs.pickle", "wb") as file:
        pickle.dump(spindle, file)


pickle_discs(collection)


def unpickle_discs(unspindle):
    with open(unspindle, "rb") as file:
        return pickle.load(file)


discs = unpickle_discs("discs.pickle")

for disc in discs:
    print(disc)
