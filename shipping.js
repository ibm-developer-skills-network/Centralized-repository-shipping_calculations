function calculateShipping(weight, distance) {
    const baseRate = 5.00;
    const ratePerKg = 1.50;
    const ratePerKm = 0.05;
    
    let totalCost = baseRate + (weight * ratePerKg) + (distance * ratePerKm);
    return totalCost.toFixed(2);
}

module.exports = { calculateShipping };