import numpy as np
import matplotlib.pyplot as plt

class CommunitySimulation:
    def __init__(self, width=50, height=40, initial_members=150, max_population=200, cost_increase=0.03):
        self.width = width
        self.height = height
        self.grid = np.zeros((height, width))
        self.community_members = []
        self.year = 1940
        self.month = 1
        self.min_stay_threshold = 0.00
        self.max_stay_threshold = 0.65
        self.threshold_difference = 0.15
        self.spawn_rate = 2
        self.base_leave_rate = 1
        self.max_population = max_population
        self.initial_members = initial_members
        self.max_monthly_departure = 3
        self.base_cost = 0.35
        self.cost_increase = cost_increase  # Amount of cost increase in 1960
        self.commitment_growth_rate = 0.07  # 7% annual commitment growth

        # Initialize community members
        initial_community_value = self.calculate_community_value(initial_members)
        for _ in range(min(initial_members, self.max_population)):
            self.spawn_member(ignore_threshold=True, initial_value=initial_community_value)

    def spawn_member(self, ignore_threshold=False, initial_value=None):
        if len(self.community_members) >= self.max_population:
            return False

        empty_cells = np.where(self.grid == 0)
        if empty_cells[0].size == 0:
            return False  # No empty cells available
        
        index = np.random.randint(0, empty_cells[0].size)
        y, x = empty_cells[0][index], empty_cells[1][index]

        community_value = self.calculate_community_value(len(self.community_members))
        
        if ignore_threshold:
            stay_threshold = np.random.uniform(self.min_stay_threshold, min(self.max_stay_threshold, community_value))
        else:
            stay_threshold = np.random.uniform(self.min_stay_threshold, self.max_stay_threshold)
        
        join_threshold = stay_threshold + self.threshold_difference
        
        if ignore_threshold or community_value >= join_threshold:
            self.grid[y, x] = 1
            self.community_members.append({
                'pos': (x, y),
                'stay_threshold': stay_threshold,
                'join_threshold': join_threshold,
                'join_year': self.year
            })
            return True
        return False

    def calculate_community_value(self, population):
        if population == 0:
            return 0.001  # Minimum community value when population is zero
        return min(1, max(0.001, (population ** 2) / (self.initial_members ** 2)))

    def calculate_cost(self):
        if self.year >= 1990:
            return self.base_cost + (self.cost_increase * 2)
        if self.year >= 1960:
            return self.base_cost + self.cost_increase
        return self.base_cost

    def update(self):
        current_population = len(self.community_members)
        community_value = self.calculate_community_value(current_population)
        cost = self.calculate_cost()

        # Update member commitment
        for member in self.community_members:
            years_in_community = self.year - member['join_year']
            commitment_growth = (1 + self.commitment_growth_rate) ** years_in_community
            effective_threshold = member['stay_threshold'] / commitment_growth
            member['effective_threshold'] = max(self.min_stay_threshold, effective_threshold)

        # Calculate departures
        random_departures = min(self.base_leave_rate, current_population)
        value_based_departures = sum(1 for member in self.community_members if community_value - cost < member['effective_threshold'])
        total_departures = min(random_departures + value_based_departures, self.max_monthly_departure, current_population)

        # Remove members
        if total_departures > 0:
            leaving_indices = np.random.choice(current_population, total_departures, replace=False)
            self.community_members = [member for i, member in enumerate(self.community_members) if i not in leaving_indices]
            self.grid = np.zeros((self.height, self.width))  # Reset the grid
            for member in self.community_members:
                x, y = member['pos']
                self.grid[y, x] = 1

        # Spawn new members
        new_members = sum(self.spawn_member() for _ in range(self.spawn_rate))

        # Update time
        self.month += 1
        if self.month > 12:
            self.month = 1
            self.year += 1
            return {
                'year': self.year,
                'population': current_population,
                'community_value': community_value,
                'cost': cost
            }
        return None

    def run_simulation(self, num_years):
        annual_data = []
        for _ in range(num_years * 12):
            result = self.update()
            if result:
                annual_data.append(result)
        return annual_data

# Run the simulation
sim = CommunitySimulation()
annual_data = sim.run_simulation(85)  # Run for 85 years

# Prepare data for plotting
years = [data['year'] for data in annual_data]
membership_percentage = [data['population'] / sim.max_population for data in annual_data]
community_values = [data['community_value'] for data in annual_data]
costs = [data['cost'] for data in annual_data]

# Plot the data
plt.figure(figsize=(12, 6))
plt.plot(years, membership_percentage, label='Normalized Membership')
plt.plot(years, community_values, label='Normalized Community Value')
plt.plot(years, costs, label='Normalized Opportunity Cost')
plt.xlabel('Year')
plt.title('Membership, Community Value, and Opportunity Cost Over Time')
plt.legend()
plt.ylim(0, 1.1)  # Set y-axis limits from 0 to 1.1 (110%)
plt.grid(True)

# Remove y-axis label
plt.ylabel('')

# Add text annotation for y-axis
plt.text(-0.08, 0.5, 'Normalized Value', va='center', rotation='vertical', transform=plt.gca().transAxes)

plt.tight_layout()
plt.show()
