import connexion
import six

from swagger_server.models.random_number import RandomNumber  # noqa: E501
from swagger_server import util
import random

def get_random(distribution=None):  # noqa: E501
    """Gets a random value

    Returns random value # noqa: E501

    :param distribution: type of distribution &#x60;unif&#x60; and &#x60;normal&#x60; allowed
    :type distribution: str

    :rtype: List[RandomNumber]
    """
    # if distribution == "unif":
    #     rand = RandomNumber
    #     return random.random()
    # if distribution == "normal":
    #     return random.random()
    # else:
    #     ValueError("Not valid distribution arg.")
    rand = RandomNumber(0, random.random())
    return rand