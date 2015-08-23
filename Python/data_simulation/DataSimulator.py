import random
C = 3*10**8 # speed of light

class ObsPost:
    """
    Observation Post Station
    """
    def __init__(self,name='',sigma=0,dist=0,p_spd=C):
        """
        @param name : station name for observation post
        @param sigma : particle observation time sigma in picoseconds
        @param dist : distance traveled from the origin in meters
        @param p_spd : particle speed in meters per second

        @attr obs_time : the time of the observation
        @attr act_time : the actual time of the particle arrival
        """
        pico = 10**12
        self.name = name
        self.obs_time = random.gauss((dist / p_spd) * pico, sigma)
        self.act_time = (dist / p_spd) * pico

    def get_data(self):
        """
        @return name : station name
        @return obs_time : observation time
        @return act_time : actual time
        """
        return self.name, self.obs_time, self.act_time

    def get_data_str(self):
        """
        @return : observation line
        """
        return str(self.name), str(self.obs_time), str(self.act_time)

class DataSimulator:
    """
    Data Simulator for Station Observations
    """
    def __init__(self,s_data,spd_m=1):
        """
        @param s_data : station data
        @param spd_m : particle speed modifier
        """
        self.s_data = s_data
        self.p_spd = spd_m * C #particle speed
       
    def get_csv_observation(self):
        """
        @return : non-normalized csv record
        """
        line_parts = []
        for s in self.s_data:
            line_part = ','.join(ObsPost(s[0],s[1],s[2],self.p_spd).get_data_str())
            line_parts.append(line_part)
        return ','.join(line_parts)

    def get_observation(self,obs_num):
        """
        @param obs_num : a normalized observation number
        @output : normalized csv record
        """
        for s in self.s_data:
            name,obs,act = ObsPost(s[0],s[1],s[2],self.p_spd).get_data()
            print obs_num,',',name,',',obs,',',act

    def simulate_data(self,n):
        for i in range(1,n+1):
            self.get_observation(i)


s_data = [['L',37,0],['E',95,4.9],['G',150,5.05]]
DataSimulator(s_data,.6).simulate_data(1000)
    

        
