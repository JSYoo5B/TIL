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
