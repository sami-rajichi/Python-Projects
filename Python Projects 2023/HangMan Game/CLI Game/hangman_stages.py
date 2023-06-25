"""
Created on Sun Jun 25 12:36:30 2023

@author: Sami RAJICHI
"""

stages = [  # final state: head, torso, both arms, and both legs
    """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
    # head, torso, both arms, and one leg
    """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
    # head, torso, and both arms
    """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
    # head, torso, and one arm
    """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
    # head and torso
    """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
    # head
    """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
    # initial empty state
    """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
]
