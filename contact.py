class Contact:
    """ 
    Represents a contact in the Rolodex.

    Attributes:
        first_name (str): the contact's first name
        last_name (str): the contact's last name
        phone (str): the contact's phone number
        address (str): the contact's street address
        city (str): the contact's city
        zip (str): the contact's zip code 
    """


    def __init__(self, fn, ln, ph, addr, city, zip):
        """
        Initializes a Contact Object.

        Args:
            fn (str): first name
            ln (str): last name
            ph (str): phone number
            addr (str): street address
            city (str): city
            zip (str): zip code
        """

        #stores the contact information in the object's attributes
        self.first_name = fn
        self.last_name = ln
        self.phone = ph
        self.address = addr
        self.city = city
        self.zip = zip
    

    def __lt__(self, other):
        """
        compares two contacts by last name if equal then first name. 

        Args:
            other (Contact): another Contact object
        
        Returns:
            bool: True if self should come before other
        """
        
        #if the last names are the same then we compare the first names 
        if self.last_name == other.last_name:
            return self.first_name < other.first_name
        
        #otherwise we just compare the contacts by last name
        return self.last_name < other.last_name
    

    def __str__(self):
        """
        Returns the contact formatted for console display.

        Returns:
            str: formatted contact information
        """

        #format the contact on multiple lines for displaying to the user
        #note: i could just do \n after each one that need to be seperated just for the displaying methods
        #all f" does in this case is for readability, all it does is add it so its not doing anything special
        return (f"{self.first_name} {self.last_name}\n"
                f"{self.phone}\n"
                f"{self.address}\n"
                f"{self.city} {self.zip}")
    

    def __repr__(self):
        """
        Returns the contact formatted for the file.

        Returns:
            str: comma-seperated contact information
        """

        #format the contact as comma seperated data for addresses.txt 
        #Note: similar to above, i don't have to split it with another f" its just for readability, it can fit on the same line.
        return (f"{self.first_name},{self.last_name},{self.phone},"
                f"{self.address},{self.city},{self.zip}")
