dev = qp.device("default.qubit", wires=1)


@qp.qnode(dev)
def convert_to_rz_rx():
    ##################
    # YOUR CODE HERE #
    ##################
    qp.RZ(np.pi/2, wires=0)
    qp.RX(3 * np.pi/2, wires=0)
    qp.RZ(np.pi/4, wires=0)
    # IMPLEMENT THE CIRCUIT IN THE PICTURE USING ONLY RZ AND RX

    return qp.state()
