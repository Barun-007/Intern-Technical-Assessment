# Weekend Getaway Ranker

A Python-based recommendation system that ranks the best weekend destinations from major Indian cities using heuristic distance estimation, ratings, and popularity metrics.

## Overview

This project implements an intelligent ranking algorithm for weekend travel recommendations across India. Since precise latitude/longitude coordinates aren't available for all destinations, the system uses a clever heuristic-based distance estimation using administrative hierarchies (City → State → Zone).

## Features

- **Heuristic Distance Estimation**: Smart distance calculation based on administrative boundaries
- **Multi-Factor Ranking**: Combines proximity (40%), rating (40%), and popularity (20%)
- **City Name Standardization**: Handles common city name variations (Delhi/New Delhi, Bangalore/Bengaluru, etc.)
- **Log-Normalized Popularity**: Uses logarithmic scaling to handle review count skewness
- **Weekend-Optimized**: Prioritizes closer destinations suitable for weekend trips

## Installation

### Prerequisites
- Python 3.7+
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/Barun-007/weekend-getaway-ranker.git
cd weekend-getaway-ranker
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Ensure your dataset is available:
```
Top Indian Places to Visit.csv
```

## Usage

### Basic Usage

```python
from weekend_getaway_ranker import WeekendGetawayRanker

# Initialize the ranker with your dataset
ranker = WeekendGetawayRanker('Top Indian Places to Visit.csv')

# Get top 20 recommendations for Delhi
recommendations, error = ranker.get_recommendations('Delhi', k=20)

if error:
    print(error)
else:
    print(recommendations)
```

### Command Line Usage

Run the script directly to get recommendations for Delhi, Mumbai, and Bangalore:

```bash
python weekend_getaway_ranker.py
```

### Custom City Query

```python
# Get recommendations for any city
recommendations, error = ranker.get_recommendations('Jaipur', k=15)
```

## Algorithm Details

### Distance Estimation Heuristic

Since GPS coordinates aren't available, the system uses administrative hierarchy for distance estimation:

| Relationship | Estimated Distance | Category |
|--------------|-------------------|----------|
| Same City | 10 km | Local |
| Same State | 150 km | Weekend Trip |
| Same Zone | 500 km | Extended Trip |
| Different Zone | 1500 km | Long Distance |

### Ranking Formula

The final rank score is calculated as:

```
Rank Score = (0.4 × Proximity) + (0.4 × Rating) + (0.2 × Popularity)
```

**Component Normalization:**

1. **Proximity Score** (40% weight):
   ```
   norm_distance = 1 - (estimated_distance / 2000)
   ```
   - Closer destinations score higher
   - Maximum practical distance: 2000 km

2. **Rating Score** (40% weight):
   ```
   norm_rating = Google_rating / 5.0
   ```
   - Normalized from 0-5 Google rating scale

3. **Popularity Score** (20% weight):
   ```
   norm_popularity = log(reviews + 1) / max_log_reviews
   ```
   - Uses logarithmic scaling to reduce skewness
   - Prevents extremely popular places from dominating

### City Name Standardization

The system automatically handles common city name variations:

- Delhi → New Delhi
- Bangalore → Bengaluru
- Gurgaon → Gurugram
- Bombay → Mumbai
- Calcutta → Kolkata
- Madras → Chennai

## Dataset Requirements

The CSV file should contain the following columns:

- `Zone`: Geographic zone (North, South, East, West, etc.)
- `State`: State name
- `City`: City name
- `Name`: Destination/place name
- `Type`: Type of attraction
- `Google review rating`: Rating (0-5 scale)
- `Number of google review in lakhs`: Review count in lakhs (100,000s)

## Sample Output

```
=== Weekend Getaway Ranker Output ===

--- Top Recommendations for Delhi ---
                      Name          City            State  est_distance_km  Google review rating  rank_score
           Qutub Minar  New Delhi        Delhi               10                   4.5      0.9234
        India Gate  New Delhi        Delhi               10                   4.6      0.9189
           Lotus Temple  New Delhi        Delhi               10                   4.5      0.9156
             Taj Mahal          Agra  Uttar Pradesh              150                   4.6      0.8876
      Amber Palace        Jaipur      Rajasthan              150                   4.5      0.8654

--- Top Recommendations for Mumbai ---
                      Name          City      State  est_distance_km  Google review rating  rank_score
        Gateway of India        Mumbai Maharashtra               10                   4.4      0.9087
      Marine Drive        Mumbai Maharashtra               10                   4.5      0.9123
     Elephanta Caves        Mumbai Maharashtra               10                   4.3      0.8976
...
```

## Project Structure

```
weekend-getaway-ranker/
├── myenv                        # virtual environment
├── weekend_getaway_ranker.py    # Main ranking algorithm
├── requirements.txt              # Python dependencies
├── README.md                     # This file
├── Top Indian Places to Visit.csv  # Dataset
└── sample_output.txt            # Example outputs
```

## Technologies Used

- **Python 3.7+**
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations and logarithmic transformations
- **sys**: System-specific parameters and error handling

## Key Design Decisions

### Why Heuristic Distance?

Without GPS coordinates, we use administrative boundaries as a proxy for distance. This approach:
- Provides reasonable distance estimates
- Works with available data
- Captures travel feasibility for weekend trips
- Is computationally efficient

### Why Log-Normalized Popularity?

Popular tourist spots can have millions of reviews, creating extreme skewness. Logarithmic transformation:
- Reduces the impact of outliers
- Provides more balanced recommendations
- Prevents mega-popular sites from dominating all queries

### Why 40-40-20 Weighting?

The weighting reflects weekend travel priorities:
- **Distance (40%)**: Weekend trips require proximity
- **Rating (40%)**: Quality of experience is crucial
- **Popularity (20%)**: Social proof matters but shouldn't dominate

## Limitations

1. **Distance Estimation**: Heuristic distances are approximations, not actual road/travel distances
2. **Zone Boundaries**: Administrative zones may not perfectly reflect travel practicality
3. **No Time Constraints**: Doesn't consider actual travel time or visit duration
4. **Static Weighting**: Uses fixed weights rather than personalized preferences

## Future Enhancements

- [ ] Integrate actual GPS coordinates and real distance calculations
- [ ] Add travel time estimation using road networks
- [ ] Include accommodation price ranges
- [ ] Add seasonal/weather considerations
- [ ] Implement user preference profiles
- [ ] Support for multi-day trip planning
- [ ] Real-time data integration (weather, traffic)
- [ ] Mobile app interface

## Error Handling

The system includes robust error handling for:
- Missing CSV files
- Invalid city names
- Missing/malformed data in the dataset
- Numeric conversion errors

Example:
```python
recommendations, error = ranker.get_recommendations('InvalidCity')
if error:
    print(error)  # Output: "Source City 'InvalidCity' not found in the dataset."
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Testing

To test with different cities:

```python
test_cities = ['Hyderabad', 'Chennai', 'Kolkata', 'Pune']

for city in test_cities:
    recs, error = ranker.get_recommendations(city, k=10)
    if not error:
        print(f"\n{city}:")
        print(recs)
```

## Author

Created as part of a local travel recommendation system project for India's tourism data.

## Acknowledgments

- Dataset: India's Must-See Places
- Google Reviews data for ratings and popularity metrics
- Administrative boundary data for distance heuristics

## Support

For questions or issues, please open an issue on the GitHub repository or contact the maintainers.
