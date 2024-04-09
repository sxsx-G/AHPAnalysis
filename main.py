import numpy as np


def create_comparison_matrix(elements):
    matrix_size = int(np.sqrt(len(elements)))
    if matrix_size * matrix_size != len(elements):
        raise ValueError("Invalid number of elements. The number of elements should be a perfect square.")

    comparison_matrix = np.array(elements).reshape(matrix_size, matrix_size)
    return comparison_matrix


def create_second_layer_matrices(first_layer_matrix, second_layer_elements):
    second_layer_matrices = []
    for _ in range(len(first_layer_matrix)):
        second_layer_matrix = create_comparison_matrix(second_layer_elements)
        second_layer_matrices.append(second_layer_matrix)
    return second_layer_matrices


def calculate_weights(comparison_matrix):
    # Normalize the comparison matrix
    normalized_matrix = comparison_matrix / comparison_matrix.sum(axis=0)

    # Sum the rows of the normalized matrix
    row_sums = normalized_matrix.sum(axis=1)

    # Calculate the weights by dividing the row sums by n
    weights = row_sums / len(comparison_matrix)

    return weights


def calculate_comprehensive_weights(first_layer_weights, *second_layer_weight_matrices):
    # Initialize an array to hold the comprehensive weights
    comprehensive_weights = np.zeros(len(second_layer_weight_matrices[0]))

    # Multiply each second layer weight matrix by its corresponding first layer weight
    # and add the results to get the comprehensive weights
    for i, second_layer_weights in enumerate(second_layer_weight_matrices):
        comprehensive_weights += first_layer_weights[i] * second_layer_weights

    return comprehensive_weights


if __name__ == '__main__':
    comMat = create_comparison_matrix([1, 3, 3, 1 / 3, 1, 2, 1 / 3, 1 / 2, 1])
    weightComMat = calculate_weights(comMat)
    participate = np.array([[1, 2, 3, 3, 4, 5, 7, 7], [1 / 2, 1, 2, 2, 3, 4, 5, 5], [1 / 3, 1 / 2, 1, 2, 3, 4, 5, 6],
                            [1 / 3, 1 / 2, 1 / 2, 1, 2, 3, 4, 4], [1 / 4, 1 / 3, 1 / 3, 1 / 2, 1, 2, 3, 3],
                            [1 / 5, 1 / 4, 1 / 4, 1 / 3, 1 / 2, 1, 2, 3],
                            [1 / 7, 1 / 5, 1 / 5, 1 / 4, 1 / 3, 1 / 2, 1, 2],
                            [1 / 7, 1 / 5, 1 / 6, 1 / 4, 1 / 3, 1 / 3, 1 / 2, 1]])
    motivation = np.array([[1, 2, 3, 3, 5, 6, 8, 8], [1 / 2, 1, 2, 3, 4, 5, 7, 7], [1 / 3, 1 / 2, 1, 1, 2, 3, 4, 5, ],
                           [1 / 3, 1 / 3, 1, 1, 2, 4, 6, 6],
                           [1 / 5, 1 / 4, 1 / 2, 1 / 2, 1, 2, 3, 4], [1 / 6, 1 / 5, 1 / 3, 1 / 4, 1 / 2, 1, 2, 2],
                           [1 / 8, 1 / 7, 1 / 4, 1 / 6, 1 / 3, 1 / 2, 1, 2],
                           [1 / 8, 1 / 7, 1 / 5, 1 / 6, 1 / 4, 1 / 2, 1 / 2, 1]])
    relationship = motivation

    weightParticipate = calculate_weights(participate)
    weightMotivation = calculate_weights(motivation)
    weightRelationship = weightMotivation
    print('participation:', weightParticipate)
    print('motivation:', weightMotivation)
    print('relationship:', weightRelationship)
    print('firstLayer:', weightComMat)
    print(calculate_comprehensive_weights(weightComMat, weightParticipate, weightMotivation, weightRelationship))



