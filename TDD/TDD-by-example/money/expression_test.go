package money_test

import (
	"github.com/stretchr/testify/assert"
	"tddbe/money"
	"testing"
)

func TestSimpleAddition(t *testing.T) {
	five := money.NewDollar(5)
	sum := five.Plus(five)
	bank := money.NewBank()
	reduced := bank.Reduce(sum, "USD")
	assert.True(t, money.NewDollar(10).Equals(reduced))
}

func TestPlusReturnsSum(t *testing.T) {
	five := money.NewDollar(5)
	result := five.Plus(five)
	sum := result.(*money.Sum)
	assert.True(t, five.Equals(sum.Augend))
	assert.True(t, five.Equals(sum.Addend))
}

func TestReduceSum(t *testing.T) {
	sum := money.NewSum(money.NewDollar(3), money.NewDollar(4))
	bank := money.NewBank()
	reduced := bank.Reduce(sum, "USD")
	assert.True(t, money.NewDollar(7).Equals(reduced))
}

func TestReduceMoney(t *testing.T) {
	bank := money.NewBank()
	reduced := bank.Reduce(money.NewDollar(1), "USD")
	assert.True(t, money.NewDollar(1).Equals(reduced))
}

func TestReduceMoneyDifferentCurrency(t *testing.T) {
	bank := money.NewBank()
	bank.AddRate("CHF", "USD", 2)
	result := bank.Reduce(money.NewFranc(2), "USD")
	assert.True(t, money.NewDollar(1).Equals(result))
}

func TestMixedAddition(t *testing.T) {
	var fiveBucks money.Expression = money.NewDollar(5)
	var tenFrancs money.Expression = money.NewFranc(10)
	bank := money.NewBank()
	bank.AddRate("CHF", "USD", 2)
	result := bank.Reduce(fiveBucks.Plus(tenFrancs), "USD")
	assert.True(t, money.NewDollar(10).Equals(result))
}
