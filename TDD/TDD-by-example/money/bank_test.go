package money

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestRateDifferentCurrency(t *testing.T) {
	bank := NewBank()
	bank.AddRate("KRW", "USD", 1450)
	rate := bank.Rate("KRW", "USD")
	assert.Equal(t, 1450, rate)
}

func TestRateSameCurrency(t *testing.T) {
	bank := NewBank()
	rate := bank.Rate("USD", "USD")
	assert.Equal(t, 1, rate)
}
