import matplotlib.pyplot as plt
from matplotlib_venn import venn3

# Given data
total_people = 120
read_newsweek = 65
read_fortune = 42
read_time = 45
read_newsweek_time = 20
read_time_fortune = 25
read_time_fortune_newsweek = 15
read_all_three = 8

# Calculate the number of people who read at least one magazine
at_least_one = (
    read_newsweek + read_fortune + read_time
    - read_newsweek_time - read_time_fortune - read_time_fortune_newsweek
    + read_all_three
)

# Calculate the number of people who read exactly one magazine
exactly_one = (
    read_newsweek - (read_newsweek_time + read_time_fortune_newsweek - read_all_three) +
    read_fortune - (read_time_fortune + read_time_fortune_newsweek - read_all_three) +
    read_time - (read_newsweek_time + read_time_fortune_newsweek - read_all_three)
)

# Create a Venn diagram
venn = venn3(
    subsets=(
        read_newsweek - (read_newsweek_time + read_time_fortune_newsweek - read_all_three),
        read_fortune - (read_time_fortune + read_time_fortune_newsweek - read_all_three),
        read_time - (read_newsweek_time + read_time_fortune_newsweek - read_all_three),
        read_newsweek_time - read_all_three,
        read_time_fortune - read_all_three,
        read_time_fortune_newsweek - read_all_three,
        read_all_three
    ),
    set_labels=('Newsweek', 'Fortune', 'Time')
)

# Display the Venn diagram
plt.title('Venn Diagram of Magazine Readers')
plt.show()

# Display the calculated values
print(f"Number of people who read at least one magazine: {at_least_one}")
print(f"Number of people who read exactly one magazine: {exactly_one}")

import matplotlib.pyplot as plt
from matplotlib_venn import venn3

# Define the sizes of each set
A_size = 15
R_size = 12
W_size = 11
AW_size = 5
AR_size = 9
RW_size = 4
ARW_size = 3

# Create the Venn diagram
venn = venn3(subsets=(A_size - AR_size - AW_size + ARW_size,
                      R_size - AR_size - RW_size + ARW_size,
                      AR_size - ARW_size,
                      W_size - AW_size - RW_size + ARW_size,
                      AW_size - ARW_size,
                      RW_size - ARW_size,
                      ARW_size),
             set_labels=('A', 'R', 'W'))

# Set labels for the intersections
venn.get_label_by_id('100').set_text(A_size - AR_size - AW_size + ARW_size)
venn.get_label_by_id('010').set_text(R_size - AR_size - RW_size + ARW_size)
venn.get_label_by_id('001').set_text(W_size - AW_size - RW_size + ARW_size)
venn.get_label_by_id('110').set_text(AR_size - ARW_size)
venn.get_label_by_id('101').set_text(AW_size - ARW_size)
venn.get_label_by_id('011').set_text(RW_size - ARW_size)
venn.get_label_by_id('111').set_text(ARW_size)

# Display the Venn diagram
plt.title("Venn Diagram of Car Options")
plt.show()

# Calculate the number of cars with W only
W_only = W_size - RW_size + ARW_size

# Calculate the number of cars with A only
A_only = A_size - AR_size - AW_size + ARW_size

# Calculate the number of cars with R only
R_only = R_size - AR_size - RW_size + ARW_size

# Calculate the number of cars with both R and W but not A
R_and_W_not_A = RW_size - ARW_size

# Calculate the number of cars with both A and R but not W
A_and_R_not_W = AR_size - ARW_size

# Calculate the number of cars with only one of the options
one_option = A_only + R_only + W_only

# Calculate the number of cars with at least one option
at_least_one_option = A_size + R_size + W_size - AR_size - AW_size - RW_size + ARW_size

# Calculate the number of cars with none of the options
none_of_the_options = 25 - at_least_one_option

# Display the results
print("Number of cars with W only:", W_only)
print("Number of cars with A only:", A_only)
print("Number of cars with R only:", R_only)
print("Number of cars with both R and W but not A:", R_and_W_not_A)
print("Number of cars with both A and R but not W:", A_and_R_not_W)
print("Number of cars with only one of the options:", one_option)
print("Number of cars with at least one option:", at_least_one_option)
print("Number of cars with none of the options:", none_of_the_options)
