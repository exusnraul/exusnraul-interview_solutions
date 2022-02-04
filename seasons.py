seasons={
    'Summer':{'Apr','May','June','July'},
    'Rainy':('Aug','Sept'),
    'Autumn':('Oct','Nov'),
    'Winter':('Dec','Jan'),
    'Spring':('Feb','Mar')
}

def seasons_fn(Month):
    for key,val in seasons.items():
        if Month in [*val]:
            return key
        
print(seasons_fn('Apr')) 