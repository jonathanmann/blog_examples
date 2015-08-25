class Station:
    """Station"""
    def __init__(self,dist,tick):
        """
        Initialize station

        @param dist : distance from origin
        @param tick : precision of timing clock measurements
        """
        self.dist = dist
        self.tick = tick

class Observation:
    """Observation"""
    def __init__(self,station,obs_time):
        """
        Initialize observation

        @station : the observation station
        @obs_time : time of the station clock at observation
        """
        self.station = station
        self.obs_time = obs_time
        self.velocity_upper_bound = self.get_rate(station.dist,obs_time)
        self.velocity_lower_bound = self.get_rate(station.dist,obs_time + station.tick)


    def get_rate(self,dist,time):
        """
        Get the velocity of the observed item

        @param dist : distance traveled at observation
        @param time : time at observation

        @return : rate -- the distance divided by the time
        """
        return float(dist) / time

class BoundarySimulation:
    """Boundary Simulation"""
    def __init__(self,records):
        """
        Initialize simulation
        @param records : a list of records each containing values for distance, tick, and observation time
        """
        lower = None
        upper = None
        for r in records:
            distance = r[0]
            tick = r[1]
            obs_time = r[2]
            s = Station(distance,tick)
            o = Observation(s,obs_time)
            u = o.velocity_upper_bound
            l = o.velocity_lower_bound

            print 'upper : ', u,', lower : ',l
            if upper is None:
                upper = u
            else:
                if u < upper:
                    upper = u
            if lower is None:
                lower = l
            else:
                if l > lower:
                    lower = l

        self.lower = lower
        self.upper = upper

    def show_bounds(self):
        """
        Print the upper and lower bounds based on available observations
        """
        print "lower bound : ",self.lower,", upper bound : ", self.upper


#record format : distance, tick, time
records = [[100,10,120],[200,15,230]]
BoundarySimulation(records).show_bounds()
