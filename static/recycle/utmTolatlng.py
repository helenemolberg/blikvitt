import math



def utmToLatLng(zone, easting, northing, northernHemisphere=True):
    if not northernHemisphere:
        northing = 10000000 - northing

    a = 6378137
    e = 0.081819191
    e1sq = 0.006739497
    k0 = 0.9996

    arc = northing / k0
    mu = arc / (a * (1 - math.pow(e, 2) / 4.0 - 3 * math.pow(e, 4) / 64.0 - 5 * math.pow(e, 6) / 256.0))

    ei = (1 - math.pow((1 - e * e), (1 / 2.0))) / (1 + math.pow((1 - e * e), (1 / 2.0)))

    ca = 3 * ei / 2 - 27 * math.pow(ei, 3) / 32.0

    cb = 21 * math.pow(ei, 2) / 16 - 55 * math.pow(ei, 4) / 32
    cc = 151 * math.pow(ei, 3) / 96
    cd = 1097 * math.pow(ei, 4) / 512
    phi1 = mu + ca * math.sin(2 * mu) + cb * math.sin(4 * mu) + cc * math.sin(6 * mu) + cd * math.sin(8 * mu)

    n0 = a / math.pow((1 - math.pow((e * math.sin(phi1)), 2)), (1 / 2.0))

    r0 = a * (1 - e * e) / math.pow((1 - math.pow((e * math.sin(phi1)), 2)), (3 / 2.0))
    fact1 = n0 * math.tan(phi1) / r0

    _a1 = 500000 - easting
    dd0 = _a1 / (n0 * k0)
    fact2 = dd0 * dd0 / 2

    t0 = math.pow(math.tan(phi1), 2)
    Q0 = e1sq * math.pow(math.cos(phi1), 2)
    fact3 = (5 + 3 * t0 + 10 * Q0 - 4 * Q0 * Q0 - 9 * e1sq) * math.pow(dd0, 4) / 24

    fact4 = (61 + 90 * t0 + 298 * Q0 + 45 * t0 * t0 - 252 * e1sq - 3 * Q0 * Q0) * math.pow(dd0, 6) / 720

    lof1 = _a1 / (n0 * k0)
    lof2 = (1 + 2 * t0 + Q0) * math.pow(dd0, 3) / 6.0
    lof3 = (5 - 2 * Q0 + 28 * t0 - 3 * math.pow(Q0, 2) + 8 * e1sq + 24 * math.pow(t0, 2)) * math.pow(dd0, 5) / 120
    _a2 = (lof1 - lof2 + lof3) / math.cos(phi1)
    _a3 = _a2 * 180 / math.pi

    latitude = 180 * (phi1 - fact1 * (fact2 + fact3 + fact4)) / math.pi

    if not northernHemisphere:
        latitude = -latitude

    longitude = ((zone > 0) and (6 * zone - 183.0) or 3.0) - _a3

    return (latitude, longitude)

def converter(eastingList, northingList):
    latLongList = []
    for i in range(len(eastingList)):
        latLongList.append(utmToLatLng(32, eastingList[i], northingList[i], True))
    return latLongList

def main():
    print("Hallo")
    easting = [568278.7,
               568278.7,
               571256.6,
               571256.6,
               571060.1,
               571060.1,
               571060.1,
               569492.3,
               569492.3,
               569492.3,
               570340.7,
               570340.7,
               570340.7,
               570369.1,
               570369.1,
               570369.1,
               569940.3,
               569940.3,
               569940.3,
               570484.4,
               570484.4,
               570484.4,
               569711.9,
               569711.9,
               569018.8,
               569018.8,
               569084.4,
               569084.4,
               569084.4,
               569809.9,
               569809.9,
               569809.9,
               570561.4,
               570561.4,
               570561.4,
               570039.3,
               570039.3,
               570039.3,
               569806,
               569806,
               569539.8,
               569539.8,
               571049.5,
               571049.5,
               571049.5,
               571296.8,
               571296.8,
               571296.8,
               570753.4,
               570753.4,
               570952.2,
               570952.2,
               570691.7,
               570691.7,
               570691.7,
               568197.6,
               568197.6,
               568838.6,
               568838.6,
               568838.6,
               567933.1,
               567933.1,
               570529,
               570529,
               570529,
               569508.9,
               569508.9,
               569508.9,
               569070,
               569070,
               569070,
               569792.4,
               569792.4,
               569829.5,
               569829.5,
               569829.5,
               568201.8,
               568201.8,
               569941.2,
               569941.2,
               569941.2,
               571564.4,
               571564.4,
               571564.4,
               569303.4,
               569303.4,
               569303.4,
               571816,
               571816,
               571816,
               571646,
               571646,
               571646,
               569638.3,
               569638.3,
               569638.3,
               568339.7,
               568339.7,
               568339.7,
               568556.4,
               568556.4,
               570179.3,
               570179.3,
               570179.3,
               570195,
               570815.3,
               570815.3,
               570815.3,
               570184,
               570184,
               570184,
               570381.6,
               570381.6,
               568355.3,
               568355.3,
               568355.3,
               569299.8,
               569299.8,
               569299.8,
               568962.5,
               568962.5,
               570167.4,
               570167.4,
               569343.2,
               569343.2,
               570847.3,
               570847.3,
               570847.3,
               570451.7,
               570451.7,
               570451.7,
               569732.6,
               569732.6,
               569624.5,
               569624.5,
               569624.5,
               569983.2,
               569983.2,
               570674,
               570674,
               570050,
               570050,
               570067.2,
               570067.2,
               570067.2,
               570789,
               570789,
               570789,
               570856.2,
               570856.2,
               570856.2,
               572923.6,
               570763.7,
               574358.3,
               574022,
               574043.1,
               574043.1,
               573657.8,
               572719.9,
               557390.3,
               558291.9,
               558291.9,
               567436.4,
               567436.4,
               567877.8,
               567528.2,
               567478.2,
               567863,
               571189.4,
               571189.4,
               574162.3,
               568794.5,
               568794.5,
               568794.5,
               568792.9,
               568792.9,
               567371.9,
               567261.3,
               566924,
               567047.1,
               567535.3,
               567174,
               567174,
               567174,
               566870.7,
               570404.5,
               570404.5,
               573645,
               573645,
               575286,
               575286,
               574965.7,
               574965.7,
               574965.7,
               575112,
               575112,
               575112,
               567636.2,
               568571,
               567881.2,
               567336,
               567860,
               567860,
               568507.2,
               568291.1,
               568051,
               567474,
               568372.1,
               567032.8,
               568011.3,
               568011.3,
               568011.3,
               567731.4,
               568741,
               574589.9,
               574364,
               574565,
               566764.1,
               566764.1,
               566764.1,
               571915.6,
               574499.5,
               574499.5,
               574499.5,
               574387.7,
               574387.7,
               574387.7,
               568882.7,
               566737.6,
               566737.6,
               572827,
               572827,
               572753,
               571872.4,
               572658.7,
               572658.7,
               572836,
               572836,
               572836,
               572030.3,
               572030.3,
               572030.3,
               571966.1,
               565377.7,
               570585.1,
               569958.3,
               569912,
               569912,
               572732,
               572732,
               571408,
               571408,
               571408,
               571617.6,
               571617.6,
               566242,
               566242,
               566242,
               571864.7,
               573943.9,
               571409.3,
               571739.5,
               572242.8,
               570778.8,
               571318.6,
               576696.5,
               576696.5,
               570119.9,
               576239.8,
               572130.2,
               572130.2,
               572217.7,
               576649,
               576649,
               576545.5,
               576092,
               576092,
               576092,
               575997.4,
               575997.4,
               562650.9,
               571535.7,
               571535.7,
               571517,
               568223,
               568223,
               570796.2,
               570796.2,
               567625.6,
               567805.8,
               567912.3,
               567377,
               567377,
               567792,
               569805.1,
               569805.1,
               566552.8,
               566552.8,
               566552.8,
               571755.1,
               571712.2,
               570956.8,
               573167.3,
               573167.3,
               573167.3,
               572430,
               571692.3,
               569714.3,
               569648.7,
               569648.7,
               572446,
               570353,
               570353,
               570059.3,
               570059.3,
               570059.3,
               570148.6,
               570148.6,
               569980,
               569980,
               569870.5,
               569577.1,
               569325.7,
               569485.4,
               569437.3,
               566870.6,
               566870.6,
               566870.6,
               572168.2,
               572031.5,
               572031.5,
               572031.5,
               576787.1,
               572208,
               570972.3]
    northing = [7034211,
                7034211,
                7035300.3,
                7035300.3,
                7035170.7,
                7035170.7,
                7035170.7,
                7033861.7,
                7033861.7,
                7033861.7,
                7034468.1,
                7034468.1,
                7034468.1,
                7034661.6,
                7034661.6,
                7034661.6,
                7034474.9,
                7034474.9,
                7034474.9,
                7035007.4,
                7035007.4,
                7035007.4,
                7032878.6,
                7032878.6,
                7034112.2,
                7034112.2,
                7034179.6,
                7034179.6,
                7034179.6,
                7034136.5,
                7034136.5,
                7034136.5,
                7034271.3,
                7034271.3,
                7034271.3,
                7034786.2,
                7034786.2,
                7034786.2,
                7034787.8,
                7034787.8,
                7034701,
                7034701,
                7034908.2,
                7034908.2,
                7034908.2,
                7034975.6,
                7034975.6,
                7034975.6,
                7034865.4,
                7034865.4,
                7035024.7,
                7035024.7,
                7034484.2,
                7034484.2,
                7034484.2,
                7034186.3,
                7034186.3,
                7034310.1,
                7034310.1,
                7034310.1,
                7034359.2,
                7034359.2,
                7034654.8,
                7034654.8,
                7034654.8,
                7033456.1,
                7033456.1,
                7033456.1,
                7033676,
                7033676,
                7033676,
                7032908.8,
                7032908.8,
                7032769.4,
                7032769.4,
                7032769.4,
                7034186.2,
                7034186.2,
                7033392.1,
                7033392.1,
                7033392.1,
                7035537,
                7035537,
                7035537,
                7034220.1,
                7034220.1,
                7034220.1,
                7035768,
                7035768,
                7035768,
                7035601,
                7035601,
                7035601,
                7032900.1,
                7032900.1,
                7032900.1,
                7034316.7,
                7034316.7,
                7034316.7,
                7034290.6,
                7034290.6,
                7034382.7,
                7034382.7,
                7034382.7,
                7034476,
                7034827.7,
                7034827.7,
                7034827.7,
                7034200,
                7034200,
                7034200,
                7034406.7,
                7034406.7,
                7033911.5,
                7033911.5,
                7033911.5,
                7034502.2,
                7034502.2,
                7034502.2,
                7034377.8,
                7034377.8,
                7034020.4,
                7034020.4,
                7034487.8,
                7034487.8,
                7035100.9,
                7035100.9,
                7035100.9,
                7034898.4,
                7034898.4,
                7034898.4,
                7033161.9,
                7033161.9,
                7033012.1,
                7033012.1,
                7033012.1,
                7033622.1,
                7033622.1,
                7034783.6,
                7034783.6,
                7033815,
                7033815,
                7033863.9,
                7033863.9,
                7033863.9,
                7034701,
                7034701,
                7034701,
                7034769.9,
                7034769.9,
                7034769.9,
                7032804.1,
                7032570.2,
                7025398.7,
                7032802,
                7033118.5,
                7033118.5,
                7033043.9,
                7032994.2,
                7033520.3,
                7025755.4,
                7025755.4,
                7032865.2,
                7032865.2,
                7030737.8,
                7032662.8,
                7032370.7,
                7031703.6,
                7034443.9,
                7034443.9,
                7033879.7,
                7026500.3,
                7026500.3,
                7026500.3,
                7026623.6,
                7026623.6,
                7033907,
                7028256.3,
                7028574.5,
                7028285,
                7028096.8,
                7027806,
                7027806,
                7027806,
                7028133.9,
                7029595.8,
                7029595.8,
                7020271,
                7020271,
                7034936.3,
                7034936.3,
                7034879.5,
                7034879.5,
                7034879.5,
                7034934,
                7034934,
                7034934,
                7029508.8,
                7030135.7,
                7030201.3,
                7023130,
                7025537.9,
                7025537.9,
                7026214,
                7025253.9,
                7025298,
                7026432,
                7027627,
                7026878.2,
                7034196,
                7034196,
                7034196,
                7034336.3,
                7025944.2,
                7032803.1,
                7033555,
                7033435,
                7024865.6,
                7024865.6,
                7024865.6,
                7020581.4,
                7020077.3,
                7020077.3,
                7020077.3,
                7019809.1,
                7019809.1,
                7019809.1,
                7028976.1,
                7031294.4,
                7031294.4,
                7035819,
                7035819,
                7036357.3,
                7035894.9,
                7035766.8,
                7035766.8,
                7035656,
                7035656,
                7035656,
                7035791.9,
                7035791.9,
                7035791.9,
                7036185.7,
                7022489.6,
                7032413.7,
                7032206.1,
                7032053,
                7032053,
                7035182,
                7035182,
                7033024.3,
                7033024.3,
                7033024.3,
                7035764.2,
                7035764.2,
                7025122,
                7025122,
                7025122,
                7029846,
                7032689.4,
                7032379,
                7032105.8,
                7031950.4,
                7032047.2,
                7031359.2,
                7034187.5,
                7034187.5,
                7031091.3,
                7033482.3,
                7031537.8,
                7031537.8,
                7034714.1,
                7033977,
                7033977,
                7033402.9,
                7034287,
                7034287,
                7034287,
                7034151.5,
                7034151.5,
                7025797.9,
                7029970.7,
                7029970.7,
                7030681.1,
                7028490.9,
                7028490.9,
                7034070.5,
                7034070.5,
                7027497.3,
                7026684.1,
                7027154.5,
                7027155,
                7027155,
                7026686,
                7027417.9,
                7027417.9,
                7029449.2,
                7029449.2,
                7029449.2,
                7030869.6,
                7031224.3,
                7035234.9,
                7033065.7,
                7033065.7,
                7033065.7,
                7034401,
                7032612.6,
                7031804.1,
                7031090.6,
                7031090.6,
                7035161,
                7025856,
                7025856,
                7026288.6,
                7026288.6,
                7026288.6,
                7026062.2,
                7026062.2,
                7025856,
                7025856,
                7026602.3,
                7026553.7,
                7026883.1,
                7026675.1,
                7026690.2,
                7030345.7,
                7030345.7,
                7030345.7,
                7034017.2,
                7033631.9,
                7033631.9,
                7033631.9,
                7032441,
                7032066,
                7034751.9]
    a = converter(easting, northing)
    print(a)
    return a


main();


