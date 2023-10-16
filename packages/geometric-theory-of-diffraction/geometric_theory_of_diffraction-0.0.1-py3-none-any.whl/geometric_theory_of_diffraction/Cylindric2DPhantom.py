import numpy as np
import pandas as pd


class Cylindric2DPhantom():
    SPEED_OF_LIGHT = 3 * 10 ** 8

    AIRY_TABLE = pd.DataFrame(
        columns=['an', 'anp', 'ai_anp', 'aip_an'],
        index=np.arange(10) + 1,
        data=np.array([
            [2.338, 1.019, 0.536, 0.701],
            [3.008, 3.248, -0.419, -0.803],
            [5.521, 4.82, 0.38, 0.865],
            [6.787, 6.163, -0.358, -0.911],
            [7.944, 7.372, 0.342, 0.947],
            [9.023, 8.488, -0.33, -0.978],
            [10.04, 9.535, 0.321, 1.004],
            [11.009, 10.528, -0.313, -1.028],
            [11.936, 11.475, 0.307, 1.049],
            [12.829, 12.385, -0.3, -1.068]
        ])
    )

    def __init__(self, position=None, radius=None):
        self.set_position(position)
        self.set_radius(radius)

    def set_position(self, position):
        self.position = position

    def set_radius(self, radius):
        self.radius = radius

    def get_position(self):
        return self.position

    def get_radius(self):
        return self.radius

    def calc_constants(self, carrier_frequency):
        """Calculate constant variables - k, D, and O - needed for calculating the shadowing gain.

        Variable k is a float while D and O are ndarray of the same size as the number of Airy function zeros.

        :param carrier_frequency: Carrier frequency in Hz.
        :type carrier_frequency: int or float
        :return: List containing k, D, and O variables
        :rtype: [float, ndarray, ndarray]
        """

        [n_min, n_max] = [1, 10]  # From 1 to 10, min and max values are included

        k = 2 * np.pi * carrier_frequency / self.SPEED_OF_LIGHT
        M = (k * self.get_radius() / 2) ** (1 / 3)
        D = 2 * M * self.AIRY_TABLE['aip_an'].loc[n_min:n_max] ** (-2) * np.exp(1j * np.pi / 6)
        O = self.AIRY_TABLE['an'].loc[n_min:n_max] / self.get_radius() * M * np.exp(1j * np.pi / 6)

        return [k, D, O]

    def calc_edge_path_distance_to_receiver(self, rx_position):
        """Calculate the distance between the receiver and the phantom's edge.

        :param rx_position:  Position of the receiver in 2D cartesian coordinates.
        :type rx_position: ndarray
        :return: Distance between the receiver and the edge of the phantom in its FOV.
        :rtype: float
        """

        p = np.linalg.norm(rx_position - self.get_position())  # Distance from rx to center
        s = (p ** 2 - self.get_radius() ** 2) ** (0.5)
        return s

    def calc_skin_propagation_distances(self, tx_position, rx_position):
        """Calculate the distance radio waves travel along the cylinders outer wall.

        :param tx_position: Position of the transmitter in 2D cartesian coordinates.
        :type tx_position: ndarray
        :param rx_position: Position of the receiver in 2D cartesian coordinates.
        :type rx_position: ndarray
        :return: Skin propagation distance along both sides of the cylinder.
        :rtype: list of floats
        """
        phantom_to_tx_vector = self.get_position() - tx_position
        phantom_to_rx_vector = self.get_position() - rx_position

        interception_angle = np.arccos(
            np.dot(phantom_to_tx_vector, phantom_to_rx_vector) / \
            (np.linalg.norm(phantom_to_tx_vector) * np.linalg.norm(phantom_to_rx_vector))
        )

        cross = np.cross(phantom_to_tx_vector, phantom_to_rx_vector)

        gamma_1 = np.arccos(self.get_radius() / np.linalg.norm(phantom_to_tx_vector))
        gamma_2 = np.arccos(self.get_radius() / np.linalg.norm(phantom_to_rx_vector))

        phi1 = int(cross < 0) * (interception_angle - gamma_1 - gamma_2) + int(cross >= 0) * (
                2 * np.pi - interception_angle - gamma_1 - gamma_2)
        phi2 = int(cross < 0) * (2 * np.pi - interception_angle - gamma_1 - gamma_2) + int(cross >= 0) * (
                interception_angle - gamma_1 - gamma_2)

        t1 = phi1 * self.get_radius()
        t2 = phi2 * self.get_radius()

        return [t1, t2]

    def calc_shadowing_gain(self, tx_position, rx_position, carrier_frequency):
        """Calculate the shadowing gain caused by the phantom.

        :param tx_position: Position of the transmitter in 2D cartesian coordinates.
        :type tx_position: ndarray
        :param rx_position: Position of the receiver in 2D cartesian coordinates.
        :type rx_position: ndarray
        :param carrier_frequency: Carrier frequency in Hz.
        :type carrier_frequency: int or float
        :return: Shadowing gain in db.
        :rtype: float
        """
        s = self.calc_edge_path_distance_to_receiver(rx_position)
        [t1, t2] = self.calc_skin_propagation_distances(tx_position, rx_position)

        [k, D, O] = self.calc_constants(carrier_frequency)

        gain_linear = abs(np.sum(
            D * np.exp(-1j * k * s) / (8 * 1j * k * s) ** (1 / 2) *
            ( np.exp(-t1 * (1j * k + O)) + np.exp(-t2 * (1j * k + O)) )
        ))

        gain_db = 20 * np.log10(gain_linear)

        return gain_db
