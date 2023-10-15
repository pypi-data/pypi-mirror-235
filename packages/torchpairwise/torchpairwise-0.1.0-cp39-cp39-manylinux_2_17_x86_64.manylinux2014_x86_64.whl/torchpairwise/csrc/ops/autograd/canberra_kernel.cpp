#include "../canberra.h"

#include <torch/autograd.h>
#include <torch/types.h>

namespace torchpairwise {
    namespace ops {
        namespace {
            class CanberraDistancesFunction
                    : public torch::autograd::Function<CanberraDistancesFunction> {
            public:
                static torch::autograd::Variable forward(
                        torch::autograd::AutogradContext *ctx,
                        const torch::autograd::Variable &x1,
                        const torch::autograd::Variable &x2) {
                    at::AutoDispatchBelowADInplaceOrView g;

                    ctx->save_for_backward({x1, x2});

                    auto output = _canberra(x1, x2);

                    return output;
                }

                static torch::autograd::variable_list backward(
                        torch::autograd::AutogradContext *ctx,
                        const torch::autograd::variable_list &grad_output) {
                    auto saved = ctx->get_saved_variables();
                    auto x1 = saved[0];
                    auto x2 = saved[1];

                    auto grads = detail::__canberra_backward(
                            grad_output[0],
                            x1,
                            x2);
                    auto grad_x1 = std::get<0>(grads);
                    auto grad_x2 = std::get<1>(grads);

                    return {
                            grad_x1,
                            grad_x2,
                    };
                }
            };

            at::Tensor _canberra_autograd(
                    const at::Tensor &x1,
                    const at::Tensor &x2) {
                return CanberraDistancesFunction::apply(x1, x2);
            }
        } // namespace

        TORCH_LIBRARY_IMPL(torchpairwise, Autograd, m) {
            m.impl(
                    TORCH_SELECTIVE_NAME("torchpairwise::_canberra"),
                    TORCH_FN(_canberra_autograd));
        }
    }
}
