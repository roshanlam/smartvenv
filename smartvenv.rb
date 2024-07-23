class Smartvenv < Formula
  include Language::Python::Virtualenv

  desc "A smarter virtual environment and dependency management tool"
  homepage "https://github.com/roshanlam/smartvenv"
  url "https://files.pythonhosted.org/packages/source/s/smartvenv/smartvenv-0.1.0.tar.gz"
  sha256 "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
  license "MIT"

  depends_on "python@3.9"

  resource "pip-tools" do
    url "https://files.pythonhosted.org/packages/source/p/pip-tools/pip-tools-6.4.0.tar.gz"
    sha256 "65553a15b1ba34be5e43889345062e38fb9b219ffa23b084ca0d4c4039b6f53b"
  end

  def install
    virtualenv_install_with_resources
  end

  test do
    system bin/"smartvenv", "--version"
  end
end
